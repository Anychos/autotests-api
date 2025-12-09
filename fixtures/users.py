import pytest
from pydantic import BaseModel, EmailStr

from clients.private_builder import AuthUserSchema
from clients.users.private_user_client import PrivateUserAPIClient, get_private_user_client
from clients.users.public_user_client import PublicUserAPIClient, get_public_user_client
from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema


class UserFixture(BaseModel):
    """
    Модель для хранения данных запроса и ответа метода создания пользователя
    """
    request: CreateUserRequestSchema
    response: CreateUserResponseSchema

    @property
    def email(self) -> EmailStr:
        return self.request.email

    @property
    def password(self) -> str:
        return self.request.password

    @property
    def auth_user(self) -> AuthUserSchema:
        schema = AuthUserSchema(
            email=self.email,
            password=self.password
        )
        return schema

@pytest.fixture
def public_user_client() -> PublicUserAPIClient:
    """
    Фикстура возвращает готовый клиент для работы с публичными методами пользователей
    """
    return get_public_user_client()

@pytest.fixture
def private_user_client(function_create_user) -> PrivateUserAPIClient:
    """
    Фикстура возвращает готовый клиент для работы с приватными методами пользователей
    """
    return get_private_user_client(function_create_user.auth_user)

@pytest.fixture
def function_create_user(public_user_client: PublicUserAPIClient) -> UserFixture:
    """
    Фикстура для создания пользователя
    Она формирует запрос на создание пользователя и возвращает объект, содержащий сам запрос и ответ сервера

    :param public_user_client: Клиент для взаимодействия с публичным API пользователей
    :return: Объект фикстуры UserFixture, содержащий данные запроса и ответа
    """
    request = CreateUserRequestSchema()
    response = public_user_client.create_user(request)
    return UserFixture(request=request, response=response)
