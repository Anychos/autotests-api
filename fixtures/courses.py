import pytest
from pydantic import BaseModel

from clients.courses.courses_client import CoursesClient, get_private_courses_client
from clients.courses.courses_schema import CreateCourseRequestSchema, CreateCourseResponseSchema
from fixtures.files import FileFixture
from fixtures.users import UserFixture


class CoursesFixture(BaseModel):
    """
    Модель для хранения данных запроса и ответа метода создания курса
    """
    request: CreateCourseRequestSchema
    response: CreateCourseResponseSchema

@pytest.fixture
def courses_client(function_create_user: UserFixture) -> CoursesClient:
    """
    Фикстура возвращает готовый клиент для работы с методами курсов
    """
    return get_private_courses_client(function_create_user.auth_user)

@pytest.fixture
def function_create_course(
        courses_client: CoursesClient,
        function_create_user: UserFixture,
        function_create_file: FileFixture) -> CoursesFixture:
    """
    Фикстура для создания курса
    Она формирует запрос на создание курса и возвращает объект, содержащий сам запрос и ответ сервера

    :param courses_client: Клиент для взаимодействия с API курсов
    :param function_create_user: Фикстура для создания пользователя
    :param function_create_file: Фикстура для создания файла
    :return: Объект фикстуры CoursesFixture, содержащий данные запроса и ответа
    """
    request = CreateCourseRequestSchema(
        preview_file_id=function_create_file.response.file.id,
        created_by_user_id=function_create_user.response.user.id
    )
    response = courses_client.create_course(request)
    return CoursesFixture(request=request, response=response)