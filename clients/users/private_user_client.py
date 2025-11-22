from httpx import Response
from clients.base_client import BaseClient
from clients.private_builder import get_private_client, AuthUserSchema
from clients.users.users_schema import UpdateUserRequestSchema, GerUserResponseSchema


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

    def get_user_by_id(self, user_id: str) -> GerUserResponseSchema:
        """
        Функция для получения сущности пользователя

        :param user_id: id пользователя
        :return: ответ сервера
        """
        response = self.get_user_by_id_api(user_id)
        return GerUserResponseSchema.model_validate_json(response.text)

    def update_user_api(self, user_id: str, request_body: UpdateUserRequestSchema) -> Response:
        """
        Обновление информации о пользователе

        :param user_id: id пользователя
        :param request_body: параметры запроса
        :return: ответ сервера
        """
        return self.patch(f'/api/v1/users/{user_id}', json=request_body.model_dump(by_alias=True))

    def delete_user_api(self, user_id: str) -> Response:
        """
        Удаление пользователя по id

        :param user_id: id пользователя
        :return: ответ сервера
        """
        return self.delete(f'/api/v1/users/{user_id}')

def get_private_user_client(user: AuthUserSchema) -> PrivateUserClient:
    return PrivateUserClient(client=get_private_client(user))