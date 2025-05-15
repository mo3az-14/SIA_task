from peewee import AutoField, BooleanField, DoubleField, Model
from playhouse.db_url import connect
from pydantic import BaseModel

db = connect("mysql://root:root@localhost:3307/sia")


class PeeBaseModel(Model):
    class Meta:
        database = db


class TransactionInformation(PeeBaseModel):
    id = AutoField()
    V1 = DoubleField()
    V2 = DoubleField()
    V3 = DoubleField()
    V4 = DoubleField()
    V5 = DoubleField()
    V6 = DoubleField()
    V7 = DoubleField()
    V8 = DoubleField()
    V9 = DoubleField()
    V10 = DoubleField()
    V11 = DoubleField()
    V12 = DoubleField()
    V13 = DoubleField()
    V14 = DoubleField()
    V15 = DoubleField()
    V16 = DoubleField()
    V17 = DoubleField()
    V18 = DoubleField()
    V19 = DoubleField()
    V20 = DoubleField()
    V21 = DoubleField()
    V22 = DoubleField()
    V23 = DoubleField()
    V24 = DoubleField()
    V25 = DoubleField()
    V26 = DoubleField()
    V27 = DoubleField()
    V28 = DoubleField()
    Amount = DoubleField()
    Class = BooleanField()


# validation schema
class TransactionValidation(BaseModel):
    V1: float
    V2: float
    V3: float
    V4: float
    V5: float
    V6: float
    V7: float
    V8: float
    V9: float
    V10: float
    V11: float
    V12: float
    V13: float
    V14: float
    V15: float
    V16: float
    V17: float
    V18: float
    V19: float
    V20: float
    V21: float
    V22: float
    V23: float
    V24: float
    V25: float
    V26: float
    V27: float
    V28: float
    Amount: float


def create_tables():
    db.connect()
    db.create_tables([TransactionInformation])
    db.close()
