from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema
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