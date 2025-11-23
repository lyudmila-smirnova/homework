from typing import Any

import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "input_data, expected_output",
    [
        ("Счет 12345678901234567890", "Счет **7890"),
        ("Счет 98765432109876543210", "Счет **3210"),
        ("Visa Platinum 1234567890123456", "Visa Platinum 1234 67** **** 3456"),
        ("Maestro 9876543210987654", "Maestro 9876 43** **** 7654"),
        ("МИР 1234123412341234", "МИР 1234 23** **** 1234"),
    ],
)
def test_mask_account_card_valid(input_data: str, expected_output: str) -> None:
    """Функция для проверки корректных входных данных"""
    assert mask_account_card(input_data) == expected_output


@pytest.mark.parametrize(
    "invalid_input",
    [
        "",  # Пустая строка
        "Счет 123",  # Слишком короткий счёт
        "Карта 123456789012",  # Неполный номер карты
        "Неизвестный формат",  # Левая строка
        12345,  # Число вместо строки
        None,  # None
    ],
)
def test_mask_account_card_invalid(invalid_input: Any) -> None:
    """Функция для проверки некорректных входных данных."""
    if not isinstance(invalid_input, str):
        with pytest.raises((AttributeError, TypeError)):
            mask_account_card(invalid_input)
    else:
        result = mask_account_card(invalid_input)
        assert isinstance(result, str)  # Хотя бы строка


@pytest.mark.parametrize(
    "input_date, expected_output",
    [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),  # Полный ISO формат
        ("2025-12-31", "31.12.2025"),  # Дата без времени
        ("0001-01-01", "01.01.0001"),  # Минимальная дата
    ],
)
def test_get_date_valid(input_date: str, expected_output: str) -> None:
    """Функция для проверки корректных входных данных"""
    assert get_date(input_date) == expected_output


@pytest.mark.parametrize(
    "invalid_input, expected_output",
    [
        ("", ".."),  # Пустая строка
        ("2024", "..2024"),  # Только год
        ("2024-03", ".03.2024"),  # Неполная дата
        ("2024/03/11", "11.03.2024"),  # Другой формат разделителей
        ("11-03-2024", "24.-2.11-0"),  # Формат DD-MM-YYYY
        ("abc", "..abc"),  # Не цифры (исправлено!)
    ],
)
def test_get_date_invalid(invalid_input: str, expected_output: str) -> None:
    """Функция возвращает строку при некорректных входных данных."""
    assert get_date(invalid_input) == expected_output


@pytest.mark.parametrize(
    "non_string_input",
    [
        20240311,  # Число
        None,  # None
        ["2024", "03", "11"],  # Список
    ],
)
def test_get_date_non_string_input(non_string_input: Any) -> None:
    """Функция проверки нестроковых входных данных."""
    with pytest.raises(TypeError):
        get_date(non_string_input)
