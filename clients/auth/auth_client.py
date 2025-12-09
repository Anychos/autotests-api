import allure
from httpx import Response

from clients.auth.auth_schema import LoginRequestSchema, LoginResponseSchema, RefreshRequestSchema
from clients.base_client import BaseAPIClient
from clients.public_builder import get_public_client


class AuthAPIClient(BaseAPIClient):
    """
    Клиент для работы с методами авторизации
    """
    @allure.step("Логин пользователя")
    def login_api(self, request_body: LoginRequestSchema) -> Response:
        """
        Выполняет POST запрос для авторизации

        :param request_body: Словарь с почтой и паролем
        :return: Ответ сервера с токеном
        """
        return self.post('/api/v1/authentication/login', json=request_body.model_dump(by_alias=True))

    @allure.step("Обновление токена")
    def refresh_api(self, request_body: RefreshRequestSchema) -> Response:
        """
        Выполняет POST запрос для обновления токена

        :param request_body: Словарь с рефреш токеном
        :return: Ответ сервера с обновленным токеном
        """
        return self.post('/api/v1/authentication/refresh', json=request_body.model_dump(by_alias=True))

    @allure.step("Логин пользователя и валидация ответа по схеме")
    def login(self, request_body: LoginRequestSchema) -> LoginResponseSchema:
        response = self.login_api(request_body)
        return LoginResponseSchema.model_validate_json(response.text) # вернет объект json, не поднимет ошибку

@allure.step("Получение клиента для работы с API аутентификации")
def get_auth_client() -> AuthAPIClient:
    """
    Функция получения клиента для работы с методами авторизации

    :return: Готовый к использованию Client
    """
    return AuthAPIClient(client=get_public_client())