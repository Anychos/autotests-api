from httpx import Response

from clients.base_client import BaseClient
from clients.exercises.exercises_schema import GetExercisesQuerySchema, GetExercisesResponseSchema, \
    CreateExerciseRequestSchema, CreateExerciseResponseSchema, UpdateExerciseRequestSchema, \
    GetExerciseQuerySchema, UpdateExerciseQuerySchema, UpdateExerciseResponseSchema, DeleteExerciseQuerySchema, \
    GetExerciseResponseSchema
from clients.private_builder import AuthUserSchema, get_private_client


class ExercisesClient(BaseClient):
    """
    Клиент для работы с упражнениями
    """
    def get_exercises_api(self, query: GetExercisesQuerySchema) -> Response:
        """
        Выполняет GET запрос для получения списка упражнений

        :param query: параметры запроса
        :return: ответ сервера
        """
        return self.get("/api/v1/exercises", params=query.model_dump(by_alias=True))

    def get_exercises(self, course_id: GetExercisesQuerySchema) -> GetExercisesResponseSchema:
        response = self.get_exercises_api(course_id)
        return response.json()

    def get_exercise_api(self, query: GetExerciseQuerySchema) -> Response:
        """
        Выполняет GET запрос для получения упражнения по его id

        :param query: id упражнения
        :return: ответ сервера
        """
        return self.get(f"/api/v1/exercises/{query.exercise_id}")

    def get_exercise(self, query: GetExerciseQuerySchema) -> GetExerciseResponseSchema:
        response = self.get_exercise_api(query=query)
        return GetExerciseResponseSchema.model_validate_json(response.text)

    def create_exercise_api(self, request_body: CreateExerciseRequestSchema) -> Response:
        """
        Выполняет POST запрос для создания упражнения

        :param request_body: тело запроса
        :return: ответ сервера
        """
        return self.post("/api/v1/exercises", json=request_body.model_dump(by_alias=True))

    def create_exercise(self, request_body: CreateExerciseRequestSchema) -> CreateExerciseResponseSchema:
        response = self.create_exercise_api(request_body)
        return CreateExerciseResponseSchema.model_validate_json(response.text)

    def update_exercise_api(self, query: UpdateExerciseQuerySchema, request_body: UpdateExerciseRequestSchema) -> Response:
        """
        Выполняет PATCH запрос для обновления упражнения

        :param query: id упражнения
        :param request_body: тело запроса
        :return: ответ сервера
        """
        return self.patch(f"/api/v1/exercises/{query.exercise_id}", json=request_body.model_dump(by_alias=True))

    def update_exercise(self, exercise_id: UpdateExerciseQuerySchema, request_body: UpdateExerciseRequestSchema) -> UpdateExerciseResponseSchema:
        response = self.update_exercise_api(exercise_id, request_body)
        return UpdateExerciseResponseSchema.model_validate_json(response.text)

    def delete_exercise_api(self, query: DeleteExerciseQuerySchema) -> Response:
        """
        Выполняет DELETE запрос для удаления упражнения

        :param query: id упражнения
        :return: ответ сервера
        """
        return self.delete(f"/api/v1/exercises/{query.exercise_id}")

def get_private_exercises_client(user: AuthUserSchema) -> ExercisesClient:
    """
    Функция получения клиента для работы с упражнениями

    :return: Готовый к использованию Client
    """
    return ExercisesClient(client=get_private_client(user))