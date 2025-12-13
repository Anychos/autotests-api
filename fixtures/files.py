import pytest
from pydantic import BaseModel

from clients.files.files_client import FilesAPIClient, get_private_files_client
from clients.files.files_schema import CreateFileRequestSchema, CreateFileResponseSchema
from fixtures.users import UserFixture


class FileFixture(BaseModel):
    """
    Модель для хранения данных запроса и ответа метода создания файла
    """
    request: CreateFileRequestSchema
    response: CreateFileResponseSchema

@pytest.fixture
def files_client(function_create_user: UserFixture) -> FilesAPIClient:
    """
    Фикстура возвращает готовый клиент для работы с методами файлов
    """
    return get_private_files_client(function_create_user.auth_user)

@pytest.fixture
def function_create_file(files_client: FilesAPIClient) -> FileFixture:
    """
    Фикстура для создания файла
    Она формирует запрос на создание файла и возвращает объект, содержащий сам запрос и ответ сервера

    :param files_client: Клиент для взаимодействия с API файлов
    :return: Объект фикстуры FileFixture, содержащий данные запроса и ответа
    """
    request = CreateFileRequestSchema(upload_file='./test_data/image.png')
    response = files_client.create_file(request)
    return FileFixture(request=request, response=response)