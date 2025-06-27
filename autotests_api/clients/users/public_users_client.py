from typing import TypedDict
from httpx import Response
from clients.api_client import APIClient

class CreateUserRequest(TypedDict):
    """
    Описание структуры данных запроса на создание пользователя
    """
    email: str
    password: str
    firstName: str
    lastName: str
    middleName: str

class PublicUsersClient(APIClient):
    """Клиент для работы с /api/v1/users"""

    def create_user_api(self, request: CreateUserRequest) -> Response:
        """
        Метод для создания пользователя

        :param request: Словарь с email, password, firstName, lastName, middleName.
        :return: Ответ от сервера в виде объекта httpx.Response
        """

        response = self.post("/api/v1/users", json=request)
        return response

