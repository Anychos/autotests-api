from httpx import Response
from clients.base_client import BaseClient
from typing import TypedDict
from clients.public_builder import get_public_client


class CreateUserRequestBody(TypedDict):
    email: str
    password: str
    lastName: str
    firstName: str
    middleName: str

class User(TypedDict):
    id: str
    email: str
    lastName: str
    firstName: str
    middleName: str

class CreateUserResponse(TypedDict):
    user: User

class PublicUserClient(BaseClient):
    """
    Клиент для работы с публичными методами пользователя
    """
    def create_user_api(self, request_body: CreateUserRequestBody) -> Response:
        """
        Выполняет POST запрос для создания пользователя

        :param request_body: словарь с данными пользователя
        :return: ответ сервера
        """
        return self.post('/api/v1/users', json=request_body)

    def create_user(self, request_body: CreateUserRequestBody) -> CreateUserResponse:
        """
        Функция для получения сущности пользователя

        :param request_body: словарь с данными пользователя
        :return: ответ сервера
        """
        response = self.create_user_api(request_body)
        return response.json()

def get_public_user_client() -> PublicUserClient:
    return PublicUserClient(client=get_public_client())