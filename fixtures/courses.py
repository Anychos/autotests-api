import pytest
from pydantic import BaseModel

from clients.courses.courses_client import CoursesClient, get_private_courses_client
from clients.courses.courses_schema import CreateCourseRequestSchema, CreateCourseResponseSchema
from fixtures.files import FileFixture
from fixtures.users import UserFixture


class CoursesFixture(BaseModel):
    request: CreateCourseRequestSchema
    response: CreateCourseResponseSchema

@pytest.fixture
def courses_client(function_create_user: UserFixture) -> CoursesClient:
    return get_private_courses_client(function_create_user.auth_user)

@pytest.fixture
def function_create_course(
        courses_client: CoursesClient,
        function_create_user: UserFixture,
        function_create_file: FileFixture) -> CoursesFixture:
    request = CreateCourseRequestSchema()
    response = courses_client.create_course(request)
    return CoursesFixture(request=request, response=response)