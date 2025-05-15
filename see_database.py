from database import TransactionInformation

if __name__ == "__main__":
    transactions = TransactionInformation.select()
    for transaction in transactions:
        print(
            f"transaction id: {transaction.id} Transaction is {'' if transaction.Class else 'not '}fraud "
        )
