from typing import TypedDict
from httpx import Response
from clients.api_client import APIClient

class GetExercisePathParams(TypedDict):
    """
    Структура параметра пути для получения упражнения
    """
    exerciseId: str

class GetExercisesQuery(TypedDict):
    """
    Структура квери параметра для получения списка упражнений
    """
    courseId: str

class CreateExerciseRequestBody(TypedDict):
    """
    Структура тела запроса на создание упражнения
    """
    title: str
    maxScore: int
    minScore: int
    orderIndex: int
    description: str
    estimatedTime: int

class UpdateExercisePathParams(TypedDict):
    """
    Структура пути параметра для обновления упражнения
    """
    exerciseId: str

class UpdateExerciseRequestBody(TypedDict):
    """
    Структура тела запроса на обновление упражнения
    """
    title: str | None
    maxScore: int | None
    minScore: int | None
    orderIndex: int | None
    description: str | None
    estimatedTime: int | None

class DeleteExercisePathParams(TypedDict):
    """
    Структура пути параметра для удаления упражнения
    """
    exerciseId: str

class ExercisesClient(APIClient):
    """
    Клиент для работы с endpoint /api/v1/exercises
    """

    def get_exercises_api(self, query: GetExercisesQuery) -> Response:
        """
        Метод для получения списка упражнений курса

        :param query: Словарь с courseId
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get("/api/v1/exercises", params=query)

    def get_exercise_api(self, path: GetExercisePathParams) -> Response:
        """
        Метод для получения упражнения по идентификатору

        :param path: Словарь с exerciseId
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(f"/api/v1/exercises/{path['exerciseId']}")

    def create_exercise_api(self, request: CreateExerciseRequestBody) -> Response:
        """
        Метод для создания упражнения

        :param request: Словарь с title, maxScore, minScore, orderIndex, description, estimatedTime
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post("/api/v1/exercises", json=request)

    def update_exercise_api(self, path: UpdateExercisePathParams, request: UpdateExerciseRequestBody) -> Response:
        """
        Метод для обновления упражнения

        :param path: Словарь с exerciseId
        :param request: Словарь с title, maxScore, minScore, orderIndex, description, estimatedTime
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.patch(f"/api/v1/exercises/{path['exerciseId']}", json=request)

    def delete_exercise_api(self, path: DeleteExercisePathParams) -> Response:
        """
        Метод для удаления упражнения

        :param path: Словарь с exerciseId
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.delete(f"/api/v1/exercises/{path['exerciseId']}")
