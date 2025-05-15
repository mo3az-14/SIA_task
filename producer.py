from kafka import KafkaProducer
import json

if __name__ == "__main__":
    producer = KafkaProducer(
        bootstrap_servers=["localhost:9092"],
        value_serializer=lambda x: json.dumps(x).encode("ascii"),
    )

    with open("example.json", "rb") as f:
        event = json.load(f)
    producer.send("event", event["example"])
    producer.flush()
