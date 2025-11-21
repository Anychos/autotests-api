from httpx import Response
from clients.base_client import BaseClient
from typing import TypedDict
from clients.private_builder import AuthUserDict, get_private_client


class CreateFileRequestBody(TypedDict):
    filename: str
    directory: str
    upload_file: str

class File(TypedDict):
    id: str
    filename: str
    directory: str
    url: str

class CreateFileResponse(TypedDict):
    file: File

class FilesClient(BaseClient):
    """
    Клиент для работы с файлами
    """
    def get_file_api(self, file_id: str) -> Response:
        """
        Получение информации о файле по id

        :param file_id: id файла
        :return: ответ сервера
        """
        return self.get(f'/api/v1/files/{file_id}')

    def create_file_api(self, request_body: CreateFileRequestBody) -> Response:
        """
        Загрузка файла

        :param request_body: тело запроса
        :return: ответ сервера
        """
        return self.post(
            '/api/v1/files',
            data=request_body,
            files={'upload_file': open(request_body['upload_file'], 'rb')}
        )

    def create_file(self, request_body: CreateFileRequestBody) -> CreateFileResponse:
        """
        Загрузка файла

        :param request_body: тело запроса
        :return: ответ сервера
        """
        response = self.create_file_api(request_body)
        return response.json()

    def delete_file_api(self, file_id: str) -> Response:
        """
        Удаление файла по id

        :param file_id: id файла
        :return: ответ сервера
        """
        return self.delete(f'/api/v1/files/{file_id}')

def get_private_files_client(user: AuthUserDict) -> FilesClient:
    return FilesClient(client=get_private_client(user))