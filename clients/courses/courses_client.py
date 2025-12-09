from httpx import Response

from clients.base_client import BaseClient
from clients.courses.courses_schema import GetCoursesQuerySchema, CreateCourseRequestSchema, \
    CreateCourseResponseSchema, UpdateCourseRequestSchema
from clients.private_builder import AuthUserSchema, get_private_client


class CoursesClient(BaseClient):
    """
    Клиент для работы с курсами
    """
    def get_courses_api(self, query: GetCoursesQuerySchema) -> Response:
        """
        Получение информации о курсе по id пользователя

        :param query: id пользователя
        :return: ответ сервера с сущностью курса
        """
        return self.get('/api/v1/courses', params=query.model_dump(by_alias=True))

    def get_course_api(self, course_id: str) -> Response:
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
        return self.delete(f'/api/v1/courses/{course_id}')

def get_private_courses_client(user: AuthUserSchema) -> CoursesClient:
    """
    Функция получения клиента для работы с методами курсов

    :return: Готовый к использованию Client
    """
    return CoursesClient(client=get_private_client(user))