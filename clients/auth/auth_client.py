from httpx import Response
from clients.base_client import BaseClient
from clients.public_builder import get_public_client
from clients.auth.auth_schema import LoginRequestSchema, RefreshRequestSchema, LoginResponseSchema


class AuthClient(BaseClient):
    """
    Клиент для работы с методами авторизации
    """
    def login_api(self, request_body: LoginRequestSchema) -> Response:
        """
        Выполняет POST запрос для авторизации

        :param request_body: словарь с почтой и паролем
        :return: ответ сервера с токеном
        """
        return self.post('/api/v1/authentication/login', json=request_body.model_dump(by_alias=True))

    def refresh_api(self, request_body: RefreshRequestSchema) -> Response:
        """
        Выполняет POST запрос для обновления токена

        :param request_body: словарь с рефреш токеном
        :return: ответ сервера с обновленным токеном
        """
        return self.post('/api/v1/authentication/refresh', json=request_body.model_dump(by_alias=True))

    def login(self, request_body: LoginRequestSchema) -> LoginResponseSchema:
        """
        Функция для авторизации и получения json ответа

        :param request_body: словарь с почтой и паролем
        :return: ответ сервера в формате json
        """
        response = self.login_api(request_body)
        return LoginResponseSchema.model_validate_json(response.text) # вернет объект json, не поднимет ошибку

def get_auth_client() -> AuthClient:
    """
    Функция получения клиента для работы с методами авторизации

    :return: Готовый к использованию Client
    """
    return AuthClient(client=get_public_client())