from clients.base_client import BaseClient
from httpx import Response
from clients.exercises.exercises_schema import GetExercisesReqSchema, GetExercisesResponseSchema, \
    CreateExerciseRequestSchema, CreateExercisesResponseSchema, UpdateExerciseRequestSchema, \
    UpdateExercisesResponseSchema
from clients.private_builder import AuthUserSchema, get_private_client


class ExercisesClient(BaseClient):
    """
    Клиент для работы с упражнениями
    """
    def get_exercises_api(self, query: GetExercisesReqSchema) -> Response:
        """
        Выполняет GET запрос для получения списка упражнений

        :param query: параметры запроса
        :return: ответ сервера
        """
        return self.get("/api/v1/exercises", params=query.model_dump(by_alias=True))

    def get_exercises(self, course_id: GetExercisesReqSchema) -> GetExercisesResponseSchema:
        response = self.get_exercises_api(course_id)
        return response.json()

    def get_exercise_api(self, query: GetExercisesReqSchema) -> Response:
        """
        Выполняет GET запрос для получения упражнения по его id

        :param exercise_id: id упражнения
        :return: ответ сервера
        """
        return self.get("/api/v1/exercises", params=query.model_dump(by_alias=True))

    def get_exercise(self, exercise_id: GetExercisesReqSchema) -> GetExercisesResponseSchema:
        response = self.get_exercise_api(exercise_id)
        return GetExercisesResponseSchema.model_validate_json(response.text)

    def create_exercise_api(self, request_body: CreateExerciseRequestSchema) -> Response:
        """
        Выполняет POST запрос для создания упражнения

        :param request_body: тело запроса
        :return: ответ сервера
        """
        return self.post("/api/v1/exercises", json=request_body.model_dump(by_alias=True))

    def create_exercise(self, request_body: CreateExerciseRequestSchema) -> CreateExercisesResponseSchema:
        response = self.create_exercise_api(request_body)
        return CreateExercisesResponseSchema.model_validate_json(response.text)

    def update_exercise_api(self, exercise_id: GetExercisesReqSchema, request_body: UpdateExerciseRequestSchema) -> Response:
        """
        Выполняет PATCH запрос для обновления упражнения

        :param exercise_id: id упражнения
        :param request_body: тело запроса
        :return: ответ сервера
        """
        return self.patch(f"/api/v1/exercises/{exercise_id}", json=request_body.model_dump(by_alias=True))

    def update_exercise(self, exercise_id: GetExercisesReqSchema, request_body: UpdateExerciseRequestSchema) -> UpdateExercisesResponseSchema:
        response = self.update_exercise_api(exercise_id, request_body)
        return UpdateExercisesResponseSchema.model_validate_json(response.text)

    def delete_exercise_api(self, exercise_id: str) -> Response:
        """
        Выполняет DELETE запрос для удаления упражнения

        :param exercise_id: id упражнения
        :return: ответ сервера
        """
        return self.delete(f"/api/v1/exercises/{exercise_id}")

def get_private_exercises_client(user: AuthUserSchema) -> ExercisesClient:
    return ExercisesClient(client=get_private_client(user))