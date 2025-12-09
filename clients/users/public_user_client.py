from httpx import Response

from clients.base_client import BaseClient
from clients.public_builder import get_public_client
from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema


class PublicUserClient(BaseClient):
    """
    Клиент для работы с публичными методами пользователя
    """
    def create_user_api(self, request_body: CreateUserRequestSchema) -> Response:
        """
        Выполняет POST запрос для создания пользователя

        :param request_body: словарь с данными пользователя
        :return: ответ сервера
        """
        return self.post('/api/v1/users', json=request_body.model_dump(by_alias=True))

    def create_user(self, request_body: CreateUserRequestSchema) -> CreateUserResponseSchema:
        response = self.create_user_api(request_body)
        return CreateUserResponseSchema.model_validate_json(response.text)

def get_public_user_client() -> PublicUserClient:
    """
    Функция получения клиента для работы с публичными методами

    :return: Готовый к использованию Client
    """
    return PublicUserClient(client=get_public_client())