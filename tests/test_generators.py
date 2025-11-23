import pytest
from src.generators import filter_by_currency, transaction_descriptions, card_number_generator

# тесты для filter_by_currency
@pytest.fixture
def sample_transactions():
    """Фикстура возвращает тестовые транзакции"""
    return [
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


@pytest.fixture
def empty_transactions():
    """Фикстура возвращает пустой список транзакций"""
    return []


@pytest.mark.parametrize("currency, expected_count, expected_ids", [
    ("USD", 1, [939719570]),  # Должна найти 1 USD транзакцию
    ("RUB", 2, [142264268, 873106923]),  # Должна найти 2 RUB транзакции
    ("EUR", 0, []),  # Не должна найти EUR транзакций
    ("GBP", 0, []),  # Не должна найти GBP транзакций
])
def test_filter_by_currency_parametrized(sample_transactions, currency, expected_count, expected_ids):
    """Тест 1: Параметризованная проверка фильтрации по разным валютам"""
    result = list(filter_by_currency(sample_transactions, currency))

    assert len(result) == expected_count
    # Проверяем ID найденных транзакций
    found_ids = [transaction["id"] for transaction in result]
    assert found_ids == expected_ids


def test_filter_by_currency_empty_list(empty_transactions):
    """Тест 2: Проверяем работу с пустым списком транзакций"""
    result = list(filter_by_currency(empty_transactions, "USD"))
    assert result == []


def test_filter_by_currency_returns_generator(sample_transactions):
    """Тест 3: Проверяем, что функция возвращает генератор"""
    result = filter_by_currency(sample_transactions, "USD")
    assert hasattr(result, '__iter__')
    assert not isinstance(result, list)


# тесты для transaction_descriptions
@pytest.fixture
def mixed_transactions():
    """Фикстура с транзакциями разных типов"""
    return [
        # Перевод организации
        {
            "id": 1,
            "from": "Организация Рога и копыта",
            "to": "счет 1234567890"
        },
        # Перевод со счета на счет
        {
            "id": 2,
            "from": "счет 1111111111",
            "to": "счет 2222222222"
        },
        # Обычный перевод (без специфических признаков)
        {
            "id": 3,
            "from": "неизвестный отправитель",
            "to": "неизвестный получатель"
        }
    ]

@pytest.mark.parametrize("transaction_index, expected_description", [
    (0, "Перевод организации"),      # Первая транзакция - организация
    (1, "Перевод со счета на счет"), # Вторая - счет на счет
    (2, "Перевод")                   # Третья - обычный перевод
])
def test_transaction_descriptions_parametrized(mixed_transactions, transaction_index, expected_description):
    """Тест 1: Параметризованная проверка правильности описаний"""
    descriptions = list(transaction_descriptions([mixed_transactions[transaction_index]]))
    assert descriptions[0] == expected_description

def test_transaction_descriptions_empty_list(empty_transactions):
    """Тест 2: Проверяем работу с пустым списком"""
    result = list(transaction_descriptions(empty_transactions))
    assert result == []

def test_transaction_descriptions_returns_generator(mixed_transactions):
    """Тест 3: Проверяем, что функция возвращает генератор"""
    result = transaction_descriptions(mixed_transactions)
    assert hasattr(result, '__iter__')
    assert not isinstance(result, list)


# тесты для card_number_generator
@pytest.mark.parametrize("start, stop, expected_results", [
    # Простые последовательные номера
    (1, 3, ["0000 0000 0000 0001", "0000 0000 0000 0002", "0000 0000 0000 0003"]),
    # Один номер
    (5, 5, ["0000 0000 0000 0005"]),
    # Большие числа для проверки форматирования
    (1234567890123456, 1234567890123456, ["1234 5678 9012 3456"]),
    # Нулевые значения
    (0, 1, ["0000 0000 0000 0000", "0000 0000 0000 0001"]),
])
def test_card_number_generator_parametrized(start, stop, expected_results):
    """Тест 1: Параметризованная проверка генерации номеров карт"""
    result = list(card_number_generator(start, stop))
    assert result == expected_results

@pytest.mark.parametrize("card_number, expected_format", [
    (0, "0000 0000 0000 0000"),
    (9999999999999999, "9999 9999 9999 9999"),
    (1234567812345678, "1234 5678 1234 5678"),
])
def test_card_number_generator_formatting(card_number, expected_format):
    """Тест 2: Проверяем правильность форматирования"""
    result = list(card_number_generator(card_number, card_number))
    assert result[0] == expected_format

def test_card_number_generator_returns_generator():
    """Тест 3: Проверяем, что функция возвращает генератор"""
    result = card_number_generator(1, 5)
    assert hasattr(result, '__iter__')
    assert not isinstance(result, list)

