from httpx import Response
from clients.base_client import BaseClient
from typing import TypedDict
from clients.public_builder import get_public_client


class LoginRequestBody(TypedDict):
    email: str
    password: str

class RefreshRequestBody(TypedDict):
    refreshToken: str

class Token(TypedDict):
    tokenType: str
    accessToken: str
    refreshToken: str

class LoginResponseBody(TypedDict):
    token: Token

class AuthClient(BaseClient):
    """
    Клиент для работы с методами авторизации
    """
    def login_api(self, request_body: LoginRequestBody) -> Response:
        """
        Выполняет POST запрос для авторизации

        :param request_body: словарь с почтой и паролем
        :return: ответ сервера с токеном
        """
        return self.post('/api/v1/authentication/login', json=request_body)

    def refresh_api(self, request_body: RefreshRequestBody) -> Response:
        """
        Выполняет POST запрос для обновления токена

        :param request_body: словарь с рефреш токеном
        :return: ответ сервера с обновленным токеном
        """
        return self.post('/api/v1/authentication/refresh', json=request_body)

    def login(self, request_body: LoginRequestBody) -> LoginResponseBody:
        """
        Функция для авторизации и получения json ответа

        :param request_body: словарь с почтой и паролем
        :return: ответ сервера в формате json
        """
        response = self.login_api(request_body)
        return response.json()

def get_auth_client() -> AuthClient:
    return AuthClient(client=get_public_client())