from http import HTTPStatus
import pytest

from clients.courses.courses_client import CoursesClient
from clients.courses.courses_schema import UpdateCourseRequestSchema, UpdateCourseResponseSchema
from fixtures.courses import CoursesFixture
from tools.assertions.courses import assert_update_course_response
from tools.assertions.schema import validate_json_schema
from tools.base_assertions import assert_status_code


@pytest.mark.regression
@pytest.mark.smoke
@pytest.mark.courses
@pytest.mark.positive
class TestCoursesPositive:
    def test_update_course(self, function_create_course: CoursesFixture, courses_client: CoursesClient):
        request = UpdateCourseRequestSchema()

        response = courses_client.update_course_api(function_create_course.response.course.id, request)
        response_data = UpdateCourseResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        validate_json_schema(instance=response.json(), schema=response_data.model_json_schema())
        assert_update_course_response(request, response_data)