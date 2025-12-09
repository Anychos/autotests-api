from typing import Any, Sized

import allure


@allure.step("Проверка соответствия статус кода ответа. Ожидается {expected}, получен {actual}")
def assert_status_code(actual: int, expected: int):
    """
    Функция для проверки статус кода

    :param actual: Полученный в ответе статус код
    :param expected: Ожидаемый статус код
    """
    assert actual == expected, (
        f'Некорректный код ответа. Получен: {actual}, ожидался: {expected}'
    )

@allure.step("Проверка соответствия значения в поле {field_name}. Ожидается {expected}, получен {actual}")
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

@allure.step("Проверка наличия поля {field_name} в ответе")
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

def assert_length(actual: Sized, expected: Sized, name: str):
    """
    Проверяет, что длины двух объектов совпадают.

    :param name: Название проверяемого объекта.
    :param actual: Фактический объект.
    :param expected: Ожидаемый объект.
    :raises AssertionError: Если длины не совпадают.
    """
    with allure.step("Проверка длины {name}. Ожидается {len(expected)}, фактически {len(actual)}"):
        assert len(actual) == len(expected), (
            f'Incorrect object length: "{name}". '
            f'Expected length: {len(expected)}. '
            f'Actual length: {len(actual)}'
        )