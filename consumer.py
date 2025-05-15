from pickle import load
from kafka import KafkaConsumer
import json
import pandas as pd
import warnings
from database import TransactionInformation, db, TransactionValidation


def insert_into_db(df: pd.DataFrame) -> None:
    # bulk insert the dataframe incase there are too many objects
    try:
        with db.atomic():
            TransactionInformation.insert_many(
                df.to_dict(orient="records"),
                fields=[
                    x for x in TransactionInformation._meta.columns.keys() if x != "id"
                ],
            ).execute()
    except Exception as e:
        print(e)


# suppress unwanted warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

# load pretrained model (scikit-learn pipeline)
with open("model.pkl", "rb") as f:
    model = load(f)


def validate_object(obj: dict) -> tuple[bool, dict, None | Exception]:
    try:
        TransactionValidation(**obj)
        return (True, obj, None)
    except Exception as e:
        return (False, obj, e)


if __name__ == "__main__":
    # intialize kafka consumer
    consumer = KafkaConsumer(
        "event",
        bootstrap_servers=["localhost:9092"],
        value_deserializer=lambda x: json.loads(x.decode("ascii")),
    )

    for message in consumer:
        # check if the incoming input is a list of objects
        if not isinstance(message.value, list) or (
            not all(isinstance(item, dict) for item in message.value)
        ):
            print(
                f"input: {message.value} is not in correct shape. please put the input in the shape of List[dict]"
            )
            continue

        # Schema validation for incoming messages
        temp = [(validate_object(obj)) for obj in message.value]
        valid_objects = [x[1] for x in temp if x[0]]
        invalid_objects = [(x[0], x[2]) for x in temp if not x[0]]

        # convert incoming messages to dataframe
        if len(valid_objects) > 0:
            # convert to dataframe to make it easier to deal with
            df = pd.DataFrame(valid_objects)

            # ids are not needed
            df.drop(["id"], inplace=True, axis=1, errors="ignore")

            # run classification model
            classification_result = model.predict(df)

            # add results to column dataframe
            df["Class"] = classification_result
            print(classification_result)

            insert_into_db(df)

        for obj, error in invalid_objects:
            print(f"object:{obj} has error")
            print(error)
