import pytest
from pydantic import BaseModel, EmailStr
from clients.auth.auth_client import AuthClient, get_auth_client
from clients.private_builder import AuthUserSchema
from clients.users.private_user_client import PrivateUserClient, get_private_user_client
from clients.users.public_user_client import get_public_user_client, PublicUserClient
from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema


# Модель для агрегации возвращаемых данных фикстурой function_user
class CreateUserFixture(BaseModel):
    request: CreateUserRequestSchema
    response: CreateUserResponseSchema

    @property
    def email(self) -> EmailStr:  # Быстрый доступ к email пользователя
        return self.request.email

    @property
    def password(self) -> str:  # Быстрый доступ к password пользователя
        return self.request.password

    @property
    def auth_user(self) -> AuthUserSchema:
        schema = AuthUserSchema(
            email=self.email,
            password=self.password
        )
        return schema

@pytest.fixture  # Объявляем фикстуру, по умолчанию скоуп function, то что нам нужно
def auth_client() -> AuthClient:  # Аннотируем возвращаемое фикстурой значение
    # Создаем новый API клиент для работы с аутентификацией
    return get_auth_client()

@pytest.fixture  # Объявляем фикстуру, по умолчанию скоуп function, то что нам нужно
def public_user_client() -> PublicUserClient:  # Аннотируем возвращаемое фикстурой значение
    # Создаем новый API клиент для работы с публичным API пользователей
    return get_public_user_client()

# Фикстура для создания пользователя
@pytest.fixture
# Используем фикстуру public_users_client, которая создает нужный API клиент
def function_create_user(public_user_client: PublicUserClient) -> CreateUserFixture:
    request = CreateUserRequestSchema()
    response = public_user_client.create_user(request)
    return CreateUserFixture(request=request, response=response)  # Возвращаем все нужные данные

@pytest.fixture
# Объявляем фикстуру, по умолчанию скоуп function, то что нам нужно
def private_user_client(function_create_user) -> PrivateUserClient:  # Аннотируем возвращаемое фикстурой значение
    # Создаем новый API клиент для работы с публичным API пользователей
    return get_private_user_client(function_create_user.auth_user)
