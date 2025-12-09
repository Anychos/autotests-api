from typing import Any

import allure
from httpx import URL, Client, QueryParams, Response
from httpx._types import RequestData, RequestFiles


class BaseAPIClient:
    """
    Базовый класс для работы с httpx
    """
    def __init__(self, client: Client):
        self.client = client

    @allure.step("Создание GET запроса на URL: {url}")
    def get(self,
            url: str | URL,
            params: QueryParams | None = None
            ) -> Response:
        """
        Выполняет GET запрос

        :param url: URL ресурса
        :param params: Параметры запроса
        :return: Ответ сервера
        """
        return self.client.get(url, params=params)

    @allure.step("Создание POST запроса на URL: {url}")
    def post(self,
             url: str | URL,
             json: Any | None = None,
             data: RequestData | None = None,
             files: RequestFiles | None = None
             ) -> Response:
        """
        Выполняет POST запрос

        :param url: URL ресурса
        :param json: Данные в формате JSON
        :param data: Данные в формате x-www-form-urlencoded
        :param files: Файлы
        :return: Ответ сервера
        """
        return self.client.post(url, json=json, data=data, files=files)

    @allure.step("Создание PATCH запроса на URL: {url}")
    def patch(self,
             url: str | URL,
             json: Any | None
              ) -> Response:
        """
        Выполняет PATCH запрос

        :param url: URL ресурса
        :param json: Данные в формате JSON
        :return: Ответ сервера
        """
        return self.client.patch(url, json=json)

    @allure.step("Создание DELETE запроса на URL: {url}")
    def delete(self, url: str | URL) -> Response:
        """
        Выполняет DELETE запрос

        :param url: URL ресурса
        :return: Ответ сервера
        """
        return self.client.delete(url)