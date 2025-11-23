import pytest
from src.generators import filter_by_currency, transaction_descriptions, card_number_generator

# Тестовые данные
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


def test_filter_by_currency_basic():
    """Тест фильтрации по валюте"""
    # Фильтруем RUB транзакции
    rub_transactions = list(filter_by_currency(transactions, "RUB"))

    # Должны найтись 2 транзакции в RUB
    assert len(rub_transactions) == 2

    # Проверяем, что все отфильтрованные транзакции действительно в RUB
    for transaction in rub_transactions:
        currency_code = transaction['operationAmount']['currency']['code']
        assert currency_code == "RUB"


def test_filter_by_currency_single_result():
    """Тест фильтрации когда есть только одна подходящая транзакция"""
    usd_transactions = list(filter_by_currency(transactions, "USD"))

    # Должна найтись только 1 транзакция в USD
    assert len(usd_transactions) == 1

    # Проверяем ID найденной транзакции
    assert usd_transactions[0]['id'] == 939719570
    assert usd_transactions[0]['operationAmount']['currency']['code'] == "USD"


def test_filter_by_currency_no_matches():
    """Тест когда нет транзакций в заданной валюте"""
    eur_transactions = list(filter_by_currency(transactions, "EUR"))

    # Не должно быть найдено ни одной транзакции
    assert len(eur_transactions) == 0
    assert eur_transactions == []


def test_filter_by_currency_empty_list():
    """Тест с пустым списком транзакций"""
    empty_transactions = []
    result = list(filter_by_currency(empty_transactions, "USD"))

    # Результат должен быть пустым списком
    assert len(result) == 0
    assert result == []


def test_filter_by_currency_generator_behavior():
    """Тест поведения генератора"""
    usd_transactions = filter_by_currency(transactions, "USD")

    # Проверяем, что это действительно генератор
    assert hasattr(usd_transactions, '__iter__')
    assert hasattr(usd_transactions, '__next__')

    # Получаем первую (и единственную) транзакцию
    first_transaction = next(usd_transactions)
    assert first_transaction['id'] == 939719570

    # Пытаемся получить следующую - должна быть ошибка StopIteration
    with pytest.raises(StopIteration):
        next(usd_transactions)


def test_filter_by_currency_multiple_calls():
    """Тест многократного использования генератора"""
    rub_generator = filter_by_currency(transactions, "RUB")

    # Первый вызов - получаем все RUB транзакции
    first_call = list(rub_generator)
    assert len(first_call) == 2

    # Второй вызов того же генератора - должен быть пустым
    second_call = list(rub_generator)
    assert len(second_call) == 0


def test_filter_by_currency_missing_currency_field():
    """Тест с транзакциями, у которых отсутствуют поля валюты"""
    incomplete_transactions = [
        {"id": 1, "operationAmount": {"amount": "100.00"}},  # нет currency
        {"id": 2, "operationAmount": {"amount": "200.00", "currency": {}}},  # пустой currency
        {"id": 3},  # нет operationAmount
    ]

    # Функция не должна падать с ошибкой
    result = list(filter_by_currency(incomplete_transactions, "USD"))
    assert len(result) == 0


def test_filter_by_currency_case_sensitivity():
    """Тест чувствительности к регистру"""
    lower_case_transactions = list(filter_by_currency(transactions, "rub"))
    upper_case_transactions = list(filter_by_currency(transactions, "RUB"))

    assert len(lower_case_transactions) == 0  # "rub" != "RUB"
    assert len(upper_case_transactions) == 2  # "RUB" == "RUB"


