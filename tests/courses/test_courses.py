from http import HTTPStatus
import pytest

from clients.courses.courses_client import CoursesClient
from clients.courses.courses_schema import UpdateCourseRequestSchema, UpdateCourseResponseSchema, GetCoursesQuerySchema, \
    GetCourseByUserResponseSchema, CreateCourseRequestSchema, CreateCourseResponseSchema
from fixtures.courses import CoursesFixture
from fixtures.files import FileFixture
from fixtures.users import function_create_user, UserFixture
from tools.assertions.courses import assert_update_course_response, assert_get_courses_response, \
    assert_create_course_response
from tools.assertions.schema import validate_json_schema
from tools.base_assertions import assert_status_code


@pytest.mark.regression
@pytest.mark.smoke
@pytest.mark.courses
@pytest.mark.positive
class TestCoursesPositive:
    def test_create_course(self, courses_client: CoursesClient, function_create_user: UserFixture, function_create_file: FileFixture):
        request = CreateCourseRequestSchema(
            preview_file_id=function_create_file.response.file.id,
            created_by_user_id=function_create_user.response.user.id
        )

        response = courses_client.create_course_api(request)
        response_data = CreateCourseResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        validate_json_schema(instance=response.json(), schema=response_data.model_json_schema())
        assert_create_course_response(response_data, request)

    def test_update_course(self, function_create_course: CoursesFixture, courses_client: CoursesClient):
        request = UpdateCourseRequestSchema()

        response = courses_client.update_course_api(function_create_course.response.course.id, request)
        response_data = UpdateCourseResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        validate_json_schema(instance=response.json(), schema=response_data.model_json_schema())
        assert_update_course_response(request, response_data)

    def test_get_courses(self, courses_client: CoursesClient, function_create_user: UserFixture, function_create_course: CoursesFixture):
        query = GetCoursesQuerySchema(user_id=function_create_user.response.user.id)
        response = courses_client.get_courses_api(query)
        response_data = GetCourseByUserResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_get_courses_response(response_data, [function_create_course.response])
        validate_json_schema(instance=response.json(), schema=response_data.model_json_schema())