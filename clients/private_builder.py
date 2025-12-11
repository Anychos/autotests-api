from functools import lru_cache  # модуль для кэширования

from httpx import Client
from pydantic import BaseModel

from clients.auth.auth_client import get_auth_client
from clients.auth.auth_schema import LoginRequestSchema
from clients.event_hooks import curl_event_hook
from config import settings


class AuthUserSchema(BaseModel, frozen=True): # делаем модель неизменяемой
    """
    Описание модели запроса авторизации
    """
    email: str
    password: str

@lru_cache(maxsize=None) # кэшируем функцию
def get_private_client(user: AuthUserSchema) -> Client:
    """
    Функция создает экземпляр httpx.Client с базовыми настройками

    :return: Готовый к использованию объект httpx.Client
    """
    auth_client = get_auth_client()
    login_request = LoginRequestSchema(email=user.email, password=user.password)
    login_response = auth_client.login(login_request)
    return Client(
        timeout=settings.http_client.timeout,
        base_url=settings.http_client.url,
        headers={"Authorization": f"Bearer {login_response.token.access_token}"},
        event_hooks={"request": [curl_event_hook]}
    )