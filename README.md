# Проект "client-operation"

## Описание:

Проект "client-operation" - это программа на Python для управления базой данных клиентов и обеспечения безопасности счетов и карт клиентов. Проект предоставляет функционал для маскирования конфиденциальных данных, обработки операций и генерации тестовых данных.

## Установка:

1. Клонируйте репозиторий:
```
git@github.com:lyudmila-smirnova/homework.git
cd homework
```
2. Установите зависимости:
```
pip install -r requirements.txt
```
## Использование:

1. Откройте проект в вашей IDE.
2. Запустите необходимые модули из папки src/

### Примеры использования основных функций:
from src.masks import get_mask_card_number, get_mask_account
from src.widget import get_date, mask_account_card

1.Маскирование данных карты
masked_card = get_mask_card_number("7000792289606361")
print(masked_card)  # 7000 79** **** 6361

2.Маскирование счета
masked_account = get_mask_account("73654108430135874305")
print(masked_account)  # **4305

3.Форматирование даты
formatted_date = get_date("2024-03-15T10:30:00.000")
print(formatted_date)  # 15.03.2024

## Структура проекта:

├── src/                    # Исходный код
│   ├── masks.py           # Маскирование данных карт и счетов
│   ├── widget.py          # Виджеты для форматирования данных
│   ├── processing.py      # Обработка и фильтрация операций
│   ├── generators.py      # Генераторы тестовых данных
│   └── decorators.py      # Декораторы для логирования
├── tests/                 # Тесты
│   ├── conftest.py
│   ├── test_masks.py
│   ├── test_widget.py
│   ├── test_processing.py
│   ├── test_generators.py
│   └── test_decorators.py
├── requirements.txt       # Зависимости проекта
└── README.md             # Документация

## Тестирование:

### Запуск тестов:

Для запуска всех тестов используйте команду:
pytest

Для запуска конкретного тестового модуля:
pytest tests/test_masks.py

Для запуска с подробным выводом:
pytest -v

### Структура тестов:

1.tests/conftest.py - Фикстуры с тестовыми данными
2.tests/test_masks.py - Тесты модуля масок карт/счетов
3.tests/test_widget.py - Тесты виджетов
4.tests/test_processing.py - Тесты модуля обработки данных
5.tests/test_generators.py - Тесты функций-генераторов
6.tests/test_decorators.py - Тесты декораторов

### Покрытие кода:

http://localhost:63342/main.py/htmlcov/index.html

### Для генерации отчета о покрытии:

pytest --cov=src --cov-report=html

### Тестируемые модули:

1. Маскирование данных (masks.py)
1.1. get_mask_card_number() - генерация масок для номеров карт
1.2. get_mask_account() - маскирование номеров счетов

2. Виджеты (widget.py):
2.1. get_date() - форматирование дат
2.2. mask_account_card() - маскирование карт/счетов

3. Обработка данных (processing.py):
3.1. filter_by_state() - фильтрация операций по статусу
3.2. sort_by_date() - сортировка операций по дате

4. Генераторы (generators.py):
4.1. filter_by_currency() - фильтрация транзакций по валюте
4.2. transaction_descriptions() - определение типа перевода
4.3. card_number_generator() - генерация номеров карт

5. Декораторы (decorators.py)
5.1. log() - декоратор для логирования выполнения функций

## Документация:

Для получения дополнительной информации обратитесь к документации функций в исходном коде или запустите встроенную справку Python:
help(function_name)

## Лицензия:

Проект распространяется без лицензии. Все права защищены.