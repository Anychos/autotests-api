from httpx import Client
from clients.auth.auth_client import get_auth_client, LoginRequestBody
from typing import TypedDict


class AuthUserDict(TypedDict):
    email: str
    password: str

def get_private_client(user: AuthUserDict) -> Client:
    """
    Функция создает экземпляр httpx.Client с базовыми настройками

    :return: Готовый к использованию объект httpx.Client
    """
    auth_client = get_auth_client()
    login_request = LoginRequestBody(email=user["email"], password=user["password"])
    login_response = auth_client.login(login_request)
    return Client(
        timeout=10,
        base_url="http://localhost:8000",
        headers={"Authorization": f"Bearer {login_response['token']['accessToken']}"}
    )