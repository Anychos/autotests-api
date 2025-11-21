from clients.base_client import BaseClient
from httpx import Response
from typing import TypedDict
from clients.private_builder import AuthUserDict, get_private_client


class GetExercises(TypedDict):
    courseId: str

class CreateExerciseRequestBody(TypedDict):
    title: str
    courseId: str
    maxScore: int
    minScore: int
    orderIndex: int
    description: str
    estimatedTime: str

class UpdateExerciseRequestBody(TypedDict):
    title: str | None
    courseId: str | None
    maxScore: int | None
    minScore: int | None
    orderIndex: int | None
    description: str | None
    estimatedTime: str | None

class Exercise(TypedDict):
    id: str
    title: str
    courseId: str
    maxScore: int
    minScore: int
    orderIndex: int
    description: str
    estimatedTime: str

class GetExercisesResponseDict(TypedDict):
    exercises: list[Exercise]

class CreateExercisesResponseDict(TypedDict):
    exercise: Exercise

class UpdateExercisesResponseDict(TypedDict):
    exercise: list[Exercise]

class ExercisesClient(BaseClient):
    """
    Клиент для работы с упражнениями
    """
    def get_exercises_api(self, query: GetExercises) -> Response:
        """
        Выполняет GET запрос для получения списка упражнений

        :param query: параметры запроса
        :return: ответ сервера
        """
        return self.get("/api/v1/exercises", params=query)

    def get_exercises(self, course_id: GetExercises) -> GetExercisesResponseDict:
        response = self.get_exercises_api(course_id)
        return response.json()

    def get_exercise_api(self, query: GetExercises) -> Response:
        """
        Выполняет GET запрос для получения упражнения по его id

        :param exercise_id: id упражнения
        :return: ответ сервера
        """
        return self.get("/api/v1/exercises", params=query)

    def get_exercise(self, exercise_id: GetExercises) -> GetExercisesResponseDict:
        response = self.get_exercise_api(exercise_id)
        return response.json()

    def create_exercise_api(self, request_body: CreateExerciseRequestBody) -> Response:
        """
        Выполняет POST запрос для создания упражнения

        :param request_body: тело запроса
        :return: ответ сервера
        """
        return self.post("/api/v1/exercises", json=request_body)

    def create_exercise(self, request_body: CreateExerciseRequestBody) -> CreateExercisesResponseDict:
        response = self.create_exercise_api(request_body)
        return response.json()

    def update_exercise_api(self, exercise_id: GetExercises, request_body: UpdateExerciseRequestBody) -> Response:
        """
        Выполняет PATCH запрос для обновления упражнения

        :param exercise_id: id упражнения
        :param request_body: тело запроса
        :return: ответ сервера
        """
        return self.patch(f"/api/v1/exercises/{exercise_id}", json=request_body)

    def update_exercise(self, exercise_id: GetExercises, request_body: UpdateExerciseRequestBody) -> UpdateExercisesResponseDict:
        response = self.update_exercise_api(exercise_id, request_body)
        return response.json()

    def delete_exercise_api(self, exercise_id: str) -> Response:
        """
        Выполняет DELETE запрос для удаления упражнения

        :param exercise_id: id упражнения
        :return: ответ сервера
        """
        return self.delete(f"/api/v1/exercises/{exercise_id}")

def get_private_exercises_client(user: AuthUserDict) -> ExercisesClient:
    return ExercisesClient(client=get_private_client(user))