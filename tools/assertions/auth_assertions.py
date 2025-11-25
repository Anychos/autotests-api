from clients.auth.auth_schema import LoginResponseSchema
from tools.base_assertions import assert_value
from tools.base_assertions import assert_is_true


def assert_login_response(response: LoginResponseSchema):
    """
    Функция для проверки ответа на запрос авторизации

    :param response: Тело ответа в формате json
    """
    assert_value(response.token.token_type, "bearer", "token_type")
    assert_is_true(response.token.access_token, "access_token")
    assert_is_true(response.token.refresh_token, "refresh_token")
