import functools


def log(filename=None):
    """Декоратор для логирования выполнения функций.
    Логирует успешное выполнение функции
    или возникшие ошибки с указанием входных параметров."""

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            """Обертка функции для добавления логирования."""
            try:
                result = func(*args, **kwargs)   # Выполняем функцию
                message = f"{func.__name__} ok"  # Логируем успешное выполнение

            except Exception as e:
                message = f"{func.__name__} error: {type(e).__name__}. Inputs: {args}, {kwargs}" # Логируем ошибку
                raise e
            finally:
                # Записываем лог в файл или консоль
                if filename:
                    with open(filename, 'a', encoding='utf-8') as f:
                        f.write(message + '\n')
                else:
                    print(message)

            return result

        return wrapper

    return decorator
