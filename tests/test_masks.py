import pytest

from src.masks import get_mask_account, get_mask_card_number


def test_standard_card() -> None:
    """Функция проверки маскирования 16-значного номера карты"""
    assert get_mask_card_number("7000792289606361") == "7000 92** **** 6361"


def test_invalid_cards() -> None:
    """Проверка обработки невалидных номеров карт"""
    # Пустая строка
    assert get_mask_card_number("") == " ** **** "

    # Номер с буквами
    assert get_mask_card_number("7000ABCD89606361") == "7000 BC** **** 6361"

    # Короткий номер
    assert get_mask_card_number("123456789012") == "1234 67** **** 9012"

    # Длинный номер
    assert get_mask_card_number("12345678901234567890") == "1234 67** **** 7890"


def test_standard_account() -> None:
    """Функция проверки маскирования 20-значного номера счета"""
    assert get_mask_account("73654108430135874305") == "**4305"


def test_invalid_accounts() -> None:
    """Проверка обработки невалидных номеров счетов"""
    # Короткий номер
    assert get_mask_account("1234") == "**1234"
    assert get_mask_account("123") == "**123"

    # Пустая строка
    assert get_mask_account("") == "**"

    # Номера с нецифровыми символами (исправленные ожидания)
    assert get_mask_account("AB34") == "**AB34"
    assert get_mask_account("12-34") == "**2-34"

    # Длинные номера
    assert get_mask_account("123456789012345678901234") == "**1234"


@pytest.mark.parametrize(
    "account,expected",
    [
        ("73654108430135874305", "**4305"),  # стандартный
        ("1234", "**1234"),  # минимально допустимый
        ("", "**"),  # пустая строка
        ("12345678", "**5678"),  # средняя длина
        ("AB34CD56", "**CD56"),  # с буквами
        ("12-34-56", "**4-56"),  # с разделителями (исправлено)
    ],
    ids=["standard_20_chars", "min_4_chars", "empty", "medium_8_chars", "with_letters", "with_delimiters"],
)
def test_parametrized_account_masking(account: str, expected: str) -> None:
    """Параметризованный тест для разных форматов счетов"""
    assert get_mask_account(account) == expected
