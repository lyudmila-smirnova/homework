import pytest
import os
from src.decorators import log


def test_log_to_console_success(capsys):
    """Тест 1: Успешное выполнение функции с выводом в консоль"""

    @log()  # Без filename - вывод в консоль
    def add(a, b):
        return a + b

    result = add(2, 3)

    # Проверяем что вывелось в консоль
    captured = capsys.readouterr()

    assert result == 5
    assert "add ok" in captured.out

