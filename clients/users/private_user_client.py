from httpx import Response
from clients.base_client import BaseClient
from typing import TypedDict
from clients.private_builder import get_private_client, AuthUserDict


class UpdateUserRequestBody(TypedDict):
    email: str | None
    lastName: str | None
    firstName: str | None
    middleName: str | None

class User(TypedDict):
    id: str
    email: str
    lastName: str
    firstName: str
    middleName: str

class GetUserResponse(TypedDict):
    user: User

class PrivateUserClient(BaseClient):
    """
    Клиент для работы с методами авторизованного пользователя
    """
    def get_current_user_api(self) -> Response:
        """
        Получение информации о текущем пользователе

        :return: ответ сервера
        """
        return self.get('/api/v1/users/me')

    def get_user_by_id_api(self, user_id: str) -> Response:
        """
        Получение информации о пользователе по id

        :param user_id: id пользователя
        :return: ответ сервера
        """
        return self.get(f'/api/v1/users/{user_id}')

    def get_user_by_id(self, user_id: str) -> GetUserResponse:
        """
        Функция для получения сущности пользователя

        :param user_id: id пользователя
        :return: ответ сервера
        """
        response = self.get_user_by_id_api(user_id)
        return response.json()

    def update_user_api(self, user_id: str, request_body: UpdateUserRequestBody) -> Response:
        """
        Обновление информации о пользователе

        :param user_id: id пользователя
        :param request_body: параметры запроса
        :return: ответ сервера
        """
        return self.patch(f'/api/v1/users/{user_id}', json=request_body)

    def delete_user_api(self, user_id: str) -> Response:
        """
        Удаление пользователя по id

        :param user_id: id пользователя
        :return: ответ сервера
        """
        return self.delete(f'/api/v1/users/{user_id}')

def get_private_user_client(user: AuthUserDict) -> PrivateUserClient:
    return PrivateUserClient(client=get_private_client(user))