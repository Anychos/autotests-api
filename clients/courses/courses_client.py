from clients.base_client import BaseClient
from httpx import Response
from typing import TypedDict
from clients.private_builder import AuthUserDict, get_private_client
from clients.files.files_client import File
from clients.users.public_user_client import User


class GetCourse(TypedDict):
    userId: str

class CreateCourseRequestBody(TypedDict):
    title: str
    maxScore: int
    minScore: int
    description: str
    estimatedTime: str
    previewFileId: str
    createdByUserId: str

class UpdateCourseRequestBody(TypedDict):
    title: str | None
    maxScore: int | None
    minScore: int | None
    description: str | None
    estimatedTime: str | None
    previewFileId: str | None
    createdByUserId: str | None

class Course(TypedDict):
    id: str
    title: str
    maxScore: int
    minScore: int
    description: str
    previewFile: File
    estimatedTime: str
    createdByUser: User

class CreateCourseResponse(TypedDict):
    course: Course

class CoursesClient(BaseClient):
    """
    Клиент для работы с курсами
    """
    def get_course_by_user_api(self, query: GetCourse) -> Response:
        """
        Получение информации о курсе по id пользователя

        :param query: id пользователя
        :return: ответ сервера с сущностью курса
        """
        return self.get('/api/v1/courses', params=query)

    def get_course_by_id_api(self, course_id: str) -> Response:
        """
        Получение информации о курсе по его id

        :param course_id: id курса
        :return: ответ сервера с сущностью курса
        """
        return self.get(f'/api/v1/courses/{course_id}')

    def create_course_api(self, request_body: CreateCourseRequestBody) -> Response:
        """
        Создание курса

        :param request_body: тело запроса с данными курса
        :return: ответ сервера с сущностью созданного курса
        """
        return self.post('/api/v1/courses', json=request_body)

    def create_course(self, request_body: CreateCourseRequestBody) -> CreateCourseResponse:
        """
        Создание курса

        :param request_body: тело запроса с данными курса
        :return: ответ сервера с сущностью созданного курса
        """
        response = self.create_course_api(request_body)
        return response.json()

    def update_course_api(self, course_id: str, request_body: UpdateCourseRequestBody) -> Response:
        """
        Обновление курса

        :param course_id: id курса
        :param request_body: тело запроса с данными для обновления
        :return: ответ сервера с обновленной сущностью курса
        """
        return self.patch(f'/api/v1/courses/{course_id}', json=request_body)

    def delete_course_api(self, course_id: str) -> Response:
        """
        Удаление курса

        :param course_id: id курса
        :return: ответ сервера
        """
        return self.delete(f'/api/v1/courses/{course_id}')

def get_private_courses_client(user: AuthUserDict) -> CoursesClient:
    return CoursesClient(client=get_private_client(user))