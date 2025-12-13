import pytest

from clients.auth.auth_client import AuthAPIClient, get_auth_client


@pytest.fixture
def auth_client() -> AuthAPIClient:
    """
    Фикстура возвращает готовый клиент для работы с методами авторизации
    """
    return get_auth_client()

