import pytest

from clients.auth.auth_client import AuthClient, get_auth_client


@pytest.fixture  # Объявляем фикстуру, по умолчанию скоуп function, то что нам нужно
def auth_client() -> AuthClient:  # Аннотируем возвращаемое фикстурой значение
    # Создаем новый API клиент для работы с аутентификацией
    return get_auth_client()

