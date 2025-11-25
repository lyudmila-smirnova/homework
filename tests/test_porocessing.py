from typing import Any, List

import pytest

from src.processing import filter_by_state, sort_by_date


@pytest.mark.parametrize(
    "state, expected_ids",
    [
        ("EXECUTED", [41428829, 939719570]),
        ("CANCELED", [594226727, 615064591]),
        ("PENDING", []),
        ("", []),  # пустая строка
        (None, []),  # None вместо строки
        (123, []),  # число вместо строки
    ],
)
def test_filter_by_state_edge_cases(sample_data: List[dict], state: str, expected_ids: List[int]) -> None:
    """Проверяем нестандартные значения state."""
    result = filter_by_state(sample_data, state=state)
    assert [item["id"] for item in result] == expected_ids


@pytest.mark.parametrize(
    "state, expected_ids",
    [
        ("EXECUTED", [41428829, 939719570]),
        ("CANCELED", [594226727, 615064591]),
        ("PENDING", []),
    ],
)
def test_filter_by_state(sample_data: List[dict], state: str, expected_ids: List[int]) -> None:
    result = filter_by_state(sample_data, state=state)
    assert [item["id"] for item in result] == expected_ids


def test_sort_by_date_descending(sample_data: List[dict]) -> None:
    result = sort_by_date(sample_data)  # reverse=True по умолчанию
    assert [item["id"] for item in result] == [41428829, 615064591, 594226727, 939719570]


def test_sort_by_date_ascending(sample_data: List[dict]) -> None:
    result = sort_by_date(sample_data, reverse=False)
    assert [item["id"] for item in result] == [939719570, 594226727, 615064591, 41428829]
