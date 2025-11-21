from httpx import Client


def get_public_client() -> Client:
    """
    Функция создает экземпляр httpx.Client с базовыми настройками

    :return: Готовый к использованию объект httpx.Client
    """
    return Client(
        timeout=10,
        base_url="http://localhost:8000"
    )