from httpx import Response

from clients.base_client import BaseClient
from clients.files.files_schema import CreateFileRequestSchema, CreateFileResponseSchema
from clients.private_builder import AuthUserSchema, get_private_client


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

    def create_file_api(self, request_body: CreateFileRequestSchema) -> Response:
        """
        Загрузка файла

        :param request_body: тело запроса
        :return: ответ сервера
        """
        return self.post(
            '/api/v1/files',
            data=request_body.model_dump(by_alias=True, exclude={'upload_file'}),
            files={'upload_file': open(request_body.upload_file, 'rb')}
        )

    def create_file(self, request_body: CreateFileRequestSchema) -> CreateFileResponseSchema:
        """
        Загрузка файла

        :param request_body: тело запроса
        :return: ответ сервера
        """
        response = self.create_file_api(request_body)
        return CreateFileResponseSchema.model_validate_json(response.text)

    def delete_file_api(self, file_id: str) -> Response:
        """
        Удаление файла по id

        :param file_id: id файла
        :return: ответ сервера
        """
        return self.delete(f'/api/v1/files/{file_id}')

def get_private_files_client(user: AuthUserSchema) -> FilesClient:
    """
    Функция получения клиента для работы с методами файлов

    :return: Готовый к использованию Client
    """
    return FilesClient(client=get_private_client(user))