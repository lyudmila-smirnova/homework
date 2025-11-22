def filter_by_currency(transactions: list[dict], currency_code: str) -> list[dict]:
    """Функция фильтрует транзакции по заданной валюте."""
    result = []
    for i in range(len(transactions)):
        transaction = transactions[i]
        if transaction.get('operationAmount', {}).get('currency', {}).get('code') == currency_code:
            result.append(transaction)
    return result


transactions = [
    {
        "id": 939719570,
        "operationAmount": {
            "amount": "9824.07",
            "currency": {"code": "USD"}
        }
    },
    {
        "id": 142264268,
        "operationAmount": {
            "amount": "79114.93",
            "currency": {"code": "RUB"}
        }
    },
    {
        "id": 873106923,
        "operationAmount": {
            "amount": "43318.34",
            "currency": {"code": "RUB"}
        },
        "from": "счет 12345678901234567890",
        "to": "счет 98765432109876543210"
    }
]

usd_transactions = filter_by_currency(transactions, "USD")
print(usd_transactions)
