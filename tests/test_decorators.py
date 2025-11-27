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


def test_log_to_console_error(capsys):
    """Тест 2: Ошибка в функции с выводом в консоль"""

    @log()
    def divide(a, b):
        return a / b

    try:
        divide(10, 0)  # Вызовет ошибку деления на ноль
    except ZeroDivisionError:
        pass

    captured = capsys.readouterr()

    # Проверяем что в консоли есть информация об ошибке
    assert "divide error" in captured.out
    assert "ZeroDivisionError" in captured.out
    assert "Inputs: (10, 0)" in captured.out

