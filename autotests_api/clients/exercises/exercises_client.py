from typing import TypedDict
from httpx import Response
from clients.api_client import APIClient
from clients.private_http_builder import AuthenticationUserDict, get_private_http_client

class Exercise(TypedDict):
    """
    Структура упражнения
    """
    id: str
    title: str
    courseId: str
    maxScore: int
    minScore: int
    orderIndex: int
    description: str
    estimatedTime: str

class GetExercisesQueryDict(TypedDict):
    """
    Структура квери параметра для получения списка упражнений
    """
    courseId: str

class CreateExerciseRequestDict(TypedDict):
    """
    Структура тела запроса на создание упражнения
    """
    title: str
    courseId: str
    maxScore: int
    minScore: int
    orderIndex: int
    description: str
    estimatedTime: str

class UpdateExerciseRequestDict(TypedDict):
    """
    Структура тела запроса на обновление упражнения
    """
    title: str | None
    courseId: str | None
    maxScore: int | None
    minScore: int | None
    orderIndex: int | None
    description: str | None
    estimatedTime: int | None

class GetExercisesResponse(TypedDict):
    """
    Структура тела ответа на получение списка упражнений
    """
    exercises: list[Exercise]

class GetExerciseResponse(TypedDict):
    """
    Структура тела ответа на получение упражнения
    """
    exercise: Exercise

class UpdateExerciseResponse(TypedDict):
    """
    Структура тела ответа на обновление упражнения
    """
    exercise: Exercise

class ExercisesClient(APIClient):
    """
    Клиент для работы с endpoint /api/v1/exercises
    """

    def get_exercises_api(self, query: GetExercisesQueryDict) -> Response:
        """
        Метод для получения списка упражнений курса

        :param query: Словарь с courseId
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get("/api/v1/exercises/", params=query)

    def get_exercise_api(self, exercise_id: str) -> Response:
        """
        Метод для получения упражнения по идентификатору

        :param exercise_id: Идентификатор упражнения
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(f"/api/v1/exercises/{exercise_id}")

    def create_exercise_api(self, request: CreateExerciseRequestDict) -> Response:
        """
        Метод для создания упражнения

        :param request: Словарь с title, maxScore, minScore, orderIndex, description, estimatedTime
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post("/api/v1/exercises", json=request)

    def update_exercise_api(self, exercise_id: str, request: UpdateExerciseRequestDict) -> Response:
        """
        Метод для обновления упражнения

        :param exercise_id: Идентификатор упражнения
        :param request: Словарь с title, maxScore, minScore, orderIndex, description, estimatedTime
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.patch(f"/api/v1/exercises/{exercise_id}", json=request)

    def delete_exercise_api(self, exercise_id: str) -> Response:
        """
        Метод для удаления упражнения

        :param exercise_id: Идентификатор упражнения
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.delete(f"/api/v1/exercises/{exercise_id}")

    def create_exercise(self, request: CreateExerciseRequestDict) -> Exercise:
        response = self.create_exercise_api(request)
        return response.json()

    def get_exercises(self, course_id: str) -> GetExercisesResponse:
        response = self.get_exercises_api({"courseId": course_id})
        return response.json()

    def get_exercise(self, exercise_id: str) -> Exercise:
        response = self.get_exercise_api(exercise_id)
        return response.json()

    def update_exercise(self, exercise_id: str, request: UpdateExerciseRequestDict) -> Exercise:
        response = self.update_exercise_api(exercise_id, request)
        return response.json()

def get_exercises_client(user: AuthenticationUserDict) -> ExercisesClient:
    """
    Функция создаёт экземпляр ExercisesClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию ExercisesClient.
    """
    return ExercisesClient(client=get_private_http_client(user))