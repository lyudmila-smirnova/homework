import os

import pytest

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


def test_log_to_file_success():
    """Тест 3: Успешное выполнение функции с записью в файл"""

    @log(filename="test.txt")
    def multiply(x, y):
        return x * y

    result = multiply(4, 5)

    # Проверяем что файл создался
    assert os.path.exists("test.txt")

    # Читаем что записалось в файл
    with open("test.txt", "r") as f:
        content = f.read()

    assert "multiply ok" in content
    assert result == 20

    # Удаляем тестовый файл
    os.remove("test.txt")


def test_log_to_file_error():
    """Тест 4: Ошибка в функции с записью в файл"""

    @log(filename="error.txt")
    def faulty_func():
        raise ValueError("Ошибка!")

    try:
        faulty_func()
    except ValueError:
        pass

    # Проверяем запись ошибки в файл
    assert os.path.exists("error.txt")

    with open("error.txt", "r") as f:
        content = f.read()

    assert "faulty_func error" in content
    assert "ValueError" in content

    # Удаляем тестовый файл
    os.remove("error.txt")
