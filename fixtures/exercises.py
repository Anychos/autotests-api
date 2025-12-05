import pytest
from pydantic import BaseModel

from clients.exercises.exercises_client import ExercisesClient, get_private_exercises_client
from clients.exercises.exercises_schema import CreateExerciseRequestSchema, CreateExerciseResponseSchema
from fixtures.courses import CoursesFixture
from fixtures.users import UserFixture


class ExercisesFixture(BaseModel):
    """
    Модель для хранения данных запроса и ответа метода создания упражнения
    """
    request: CreateExerciseRequestSchema
    response: CreateExerciseResponseSchema

@pytest.fixture
def exercises_client(function_create_user: UserFixture) -> ExercisesClient:
    """
    Фикстура возвращает готовый клиент для работы с методами упражнений
    """
    return get_private_exercises_client(function_create_user.auth_user)

@pytest.fixture
def function_create_exercise(exercises_client: ExercisesClient,
                             function_create_course: CoursesFixture) -> ExercisesFixture:
    """
    Фикстура для создания упражнения
    Она формирует запрос на создание упражнения и возвращает объект, содержащий сам запрос и ответ сервера

    :param exercises_client: Клиент для взаимодействия с API упражнений
    :param function_create_course: Фикстура для создания курса
    :return: Объект фикстуры ExercisesFixture, содержащий данные запроса и ответа
    """
    request = CreateExerciseRequestSchema(course_id=function_create_course.response.course.id)
    response = exercises_client.create_exercise(request)
    return ExercisesFixture(request=request, response=response)
