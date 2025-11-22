from clients.base_client import BaseClient
from httpx import Response
from clients.courses.courses_schema import GetCourseByUserRequestSchema, CreateCourseRequestSchema, \
    CreateCourseResponseSchema, UpdateCourseRequestSchema
from clients.private_builder import AuthUserSchema, get_private_client


class CoursesClient(BaseClient):
    """
    Клиент для работы с курсами
    """
    def get_course_by_user_api(self, query: GetCourseByUserRequestSchema) -> Response:
        """
        Получение информации о курсе по id пользователя

        :param query: id пользователя
        :return: ответ сервера с сущностью курса
        """
        return self.get('/api/v1/courses', params=query.model_dump(by_alias=True))

    def get_course_by_id_api(self, course_id: str) -> Response:
        """
        Получение информации о курсе по его id

        :param course_id: id курса
        :return: ответ сервера с сущностью курса
        """
        return self.get(f'/api/v1/courses/{course_id}')

    def create_course_api(self, request_body: CreateCourseRequestSchema) -> Response:
        """
        Создание курса

        :param request_body: тело запроса с данными курса
        :return: ответ сервера с сущностью созданного курса
        """
        return self.post('/api/v1/courses', json=request_body.model_dump(by_alias=True))

    def create_course(self, request_body: CreateCourseRequestSchema) -> CreateCourseResponseSchema:
        """
        Создание курса

        :param request_body: тело запроса с данными курса
        :return: ответ сервера с сущностью созданного курса
        """
        response = self.create_course_api(request_body)
        return CreateCourseResponseSchema.model_validate_json(response.text)

    def update_course_api(self, course_id: str, request_body: UpdateCourseRequestSchema) -> Response:
        """
        Обновление курса

        :param course_id: id курса
        :param request_body: тело запроса с данными для обновления
        :return: ответ сервера с обновленной сущностью курса
        """
        return self.patch(f'/api/v1/courses/{course_id}', json=request_body.model_dump(by_alias=True))

    def delete_course_api(self, course_id: str) -> Response:
        """
        Удаление курса

        :param course_id: id курса
        :return: ответ сервера
        """
        return self.delete(f'/api/v1/courses/{course_id}')

def get_private_courses_client(user: AuthUserSchema) -> CoursesClient:
    return CoursesClient(client=get_private_client(user))