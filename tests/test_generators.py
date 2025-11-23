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


