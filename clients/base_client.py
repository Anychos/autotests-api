from httpx import Client, URL, QueryParams, Response
from typing import Any
from httpx._types import RequestData, RequestFiles


class BaseClient:
    """
    Базовый класс для работы с httpx
    """
    def __init__(self, client: Client):
        self.client = client

    def get(self,
            url: str | URL,
            params: QueryParams | None = None
            ) -> Response:
        """
        Выполняет GET запрос

        :param url: URL ресурса
        :param params: параметры запроса
        :return: ответ сервера
        """
        return self.client.get(url, params=params)

    def post(self,
             url: str | URL,
             json: Any | None = None,
             data: RequestData | None = None,
             files: RequestFiles | None = None
             ) -> Response:
        """
        Выполняет POST запрос

        :param url: URL ресурса
        :param json: данные в формате JSON
        :param data: данные в формате x-www-form-urlencoded
        :param files: файлы
        :return: ответ сервера
        """
        return self.client.post(url, json=json, data=data, files=files)

    def patch(self,
             url: str | URL,
             json: Any | None
              ) -> Response:
        """
        Выполняет PATCH запрос

        :param url: URL ресурса
        :param json: данные в формате JSON
        :return: ответ сервера
        """
        return self.client.patch(url, json=json)

    def delete(self, url: str | URL) -> Response:
        """
        Выполняет DELETE запрос

        :param url: URL ресурса
        :return: ответ сервера
        """
        return self.client.delete(url)