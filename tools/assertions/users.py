from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema, GetUserResponseSchema
from tools.base_assertions import assert_value


def assert_create_user_response(request: CreateUserRequestSchema, response: CreateUserResponseSchema):
    """
    Проверяет, что ответ на создание пользователя соответствует запросу.

    :param request: Исходный запрос на создание пользователя.
    :param response: Ответ API с данными пользователя.
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    assert_value(response.user.email, request.email, "email")
    assert_value(response.user.last_name, request.last_name, "last_name")
    assert_value(response.user.first_name, request.first_name, "first_name")
    assert_value(response.user.middle_name, request.middle_name, "middle_name")

def assert_user(actual: CreateUserResponseSchema, expected: GetUserResponseSchema):
    """
    Проверяет, что ответ на получение пользователя соответствует ответу на создание пользователя.

    :param actual: Схема ответа на создание пользователя
    :param expected: Схема ответа на получение пользователя
    """
    assert_value(expected.user.id, actual.user.id, "id")
    assert_value(expected.user.email, actual.user.email, "email")
    assert_value(expected.user.last_name, actual.user.last_name, "last_name")
    assert_value(expected.user.first_name, actual.user.first_name, "first_name")
    assert_value(expected.user.middle_name, actual.user.middle_name, "middle_name")

def assert_get_user_response(create_user_response: CreateUserResponseSchema, get_user_response: GetUserResponseSchema):
    assert_user(create_user_response, get_user_response)