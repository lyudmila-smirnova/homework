from typing import Generator

def filter_by_currency(transactions: list[dict], currency_code: str):
    """Функция фильтрует транзакции по заданной валюте."""
    for i in range(len(transactions)):
        transaction = transactions[i]
        if transaction.get('operationAmount', {}).get('currency', {}).get('code') == currency_code:
            yield transaction


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
print(type(usd_transactions))  # <class 'generator'>

# Использование как в условии задачи
for _ in range(1):
    print(next(usd_transactions))


def transaction_descriptions(transactions: list[dict]) -> str:
    """Генератор transaction_descriptions,
    который принимает список словарей с транзакциями
    и возвращает описание каждой операции по очереди"""
    for transaction in transactions:
        from_acc = transaction.get('from', '').lower()
        to_acc = transaction.get('to', '').lower()

        if 'организация' in from_acc or 'организация' in to_acc:
            yield 'Перевод организации'
        elif 'счет' in from_acc and 'счет' in to_acc:
            yield 'Перевод со счета на счет'
        elif 'карт' in from_acc and 'карт' in to_acc:
            yield 'Перевод с карты на карту'
        else:
            yield 'Перевод'


descriptions = transaction_descriptions(transactions)
for _ in range(3):
    print(next(descriptions))


def card_number_generator(start: int, end: int) -> Generator[str, None, None]:
    """Генератор, который выдает номера банковских карт в формате XXXX XXXX XXXX XXXX,
    где X— цифра номера карты."""
    for number in range(start, end + 1):
        card_str = f"{number:016d}"  # Форматируем как 16-значное число с нулями
        yield f"{card_str[:4]} {card_str[4:8]} {card_str[8:12]} {card_str[12:16]}"


result = card_number_generator(1, 5)
print(type(result))  # <class 'generator'>
print(result)
