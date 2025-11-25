from typing import Any


def assert_status_code(actual: int, expected: int):
    """
    Функция для проверки статус кода

    :param actual: Полученный в ответе статус код
    :param expected: Ожидаемый статус код
    """
    assert actual == expected, (
        f'Некорректный код ответа. Получен: {actual}, ожидался: {expected}'
    )

def assert_value(actual: Any, expected: Any, field_name: str):
    """
    Функция для проверки значения поле ответа

    :param actual: Полученное значение
    :param expected: Ожидаемое значение
    :param field_name: Наименование поля
    """
    assert actual == expected, (
        f'Некорректное значение в поле {field_name}. Получено: {actual}, ожидалось: {expected}'
    )

def assert_is_true(actual: Any, field_name: str):
    """
    Проверяет, что фактическое значение является истинным.

    :param field_name: Название проверяемого значения.
    :param actual: Фактическое значение.
    :raises AssertionError: Если фактическое значение ложно.
    """
    assert actual, (
        f'Incorrect value: "{field_name}". '
        f'Expected true value but got: {actual}'
    )