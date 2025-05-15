# Realtime credit card fraud detection: SIA task 

## 1) clone the repo:

```bash 
git clone https://github.com/mo3az-14/SIA_task.git
cd SIA_task
```

## 2) setup infrastucture: 
We will need docker and docker compose to run our infrastructure. Go to [docker](https://docs.docker.com/engine/install/) and [docker compose](https://docs.docker.com/compose/install/) and follow the installation instructures for your OS.

Run docker compose to start our infrastructure: 
```bash
docker compose up -d
```
you can proceed to step 3 while docker is pulling the images

If you want to stop the docker containers and you know you will restart it again: 
```bash 
docker compose stop
```
That way MySQL database data will be persist with every run.

If you will not use the project again and want to remove MySQL database: 
```bash 
docker compose down -v
```

## 3) python setup:
create anaconda environemnt: 
```bash 
conda create -n SIA_task python=3.12
conda activate SIA_task
```

install packages: 
```bash 
pip install -r requirements.txt
```

## 4) setup database (only once): 
Wait for a couple of seconds after starting docker compose and then run this python script **ONLY ONCE** to create the database: 
```bash
python create_tables.py
```

## 5) run the script
open 2 terminals and activate conda environment
```bash 
conda activate SIA_task
```

run consumer: 
```bash
python consumer.py
```

run producer: 

```bash
python producer.py
```

we are using the `"example"` object from the `example.json` in the producer.

I have included 10 truthy and 10 falsey examples in `"true examples"` and `"false examples"`.

Feel free to change the `"example"` by copying other examples into it. 

python snippet used to generate falsey examples:
```python
import pandas as pd

df = pd.read_csv('creditcard_2023.csv')

df[df.Class == 0 ].iloc[:10].to_json(orient="records")
```

## Notes: 
### 1. Model 
The model is a catboost classifier from the catboost library ( similar api to sklearn models ) with 99.99% accuracy.

The `model.pkl` is a scikit-learn pipeline object pickled with cloudpickle. 
### 2. Dataset
You can find the dataset from kaggle [here](https://www.kaggle.com/datasets/nelgiriyewithana/credit-card-fraud-detection-dataset-2023/)
### 3. Docker
Why Docker? The setup is way simpler that way as we don't have to download anything on our machine like JVM, kafka, MySQL, etc...docker will handle everything for us.

If we want to swap the database that will be as simple as changing the `docker-compose.yml` file and changing the connection URL!
