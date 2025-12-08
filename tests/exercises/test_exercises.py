from http import HTTPStatus
import pytest

from clients.error_schema import InternalErrorResponseSchema
from clients.exercises.exercises_client import ExercisesClient
from clients.exercises.exercises_schema import CreateExerciseRequestSchema, CreateExerciseResponseSchema, \
    GetExerciseResponseSchema, GetExerciseQuerySchema, UpdateExerciseRequestSchema, UpdateExerciseQuerySchema, \
    UpdateExerciseResponseSchema, DeleteExerciseQuerySchema, GetExercisesResponseSchema, GetExercisesQuerySchema
from fixtures.courses import CoursesFixture
from fixtures.exercises import ExercisesFixture
from tools.assertions.exercises import assert_create_exercise_response, assert_get_exercise_response, \
    assert_update_exercise_response, assert_exercise_not_found_response, assert_get_exercises_response
from tools.assertions.schema import validate_json_schema
from tools.base_assertions import assert_status_code


@pytest.mark.regression
@pytest.mark.smoke
@pytest.mark.exercises
@pytest.mark.positive
class TestExercisesPositive:
    def test_create_exercise(self, exercises_client: ExercisesClient, function_create_course: CoursesFixture):
        request = CreateExerciseRequestSchema(course_id=function_create_course.response.course.id)

        response = exercises_client.create_exercise_api(request)
        response_data = CreateExerciseResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        validate_json_schema(instance=response.json(), schema=response_data.model_json_schema())
        assert_create_exercise_response(response_data, request)

    def test_get_exercise(self, function_create_exercise: ExercisesFixture, exercises_client: ExercisesClient):
        query = GetExerciseQuerySchema(exercise_id=function_create_exercise.response.exercise.id)
        response = exercises_client.get_exercise_api(query=query)
        response_data = GetExerciseResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        validate_json_schema(instance=response.json(), schema=response_data.model_json_schema())
        assert_get_exercise_response(response_data, function_create_exercise.response)

    def test_update_exercise(self, function_create_exercise: ExercisesFixture, exercises_client: ExercisesClient):
        query = UpdateExerciseQuerySchema(exercise_id=function_create_exercise.response.exercise.id)
        request = UpdateExerciseRequestSchema()

        response = exercises_client.update_exercise_api(query=query, request_body=request)
        response_data = UpdateExerciseResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        validate_json_schema(instance=response.json(), schema=response_data.model_json_schema())
        assert_update_exercise_response(response_data, request)

    def test_delete_exercise(self, function_create_exercise: ExercisesFixture, exercises_client: ExercisesClient):
        delete_query = DeleteExerciseQuerySchema(exercise_id=function_create_exercise.response.exercise.id)
        delete_response = exercises_client.delete_exercise_api(query=delete_query)

        assert_status_code(delete_response.status_code, HTTPStatus.OK)

        get_query = GetExerciseQuerySchema(exercise_id=function_create_exercise.response.exercise.id)
        get_response = exercises_client.get_exercise_api(query=get_query)
        get_response_data = InternalErrorResponseSchema.model_validate_json(get_response.text)

        assert_status_code(get_response.status_code, HTTPStatus.NOT_FOUND)
        assert_exercise_not_found_response(actual=get_response_data)
        validate_json_schema(instance=get_response.json(), schema=get_response_data.model_json_schema())

    def test_get_exercises(self, function_create_course: CoursesFixture, function_create_exercise: ExercisesFixture, exercises_client: ExercisesClient):
        query = GetExercisesQuerySchema(course_id=function_create_course.response.course.id)
        response = exercises_client.get_exercises_api(query=query)
        response_data = GetExercisesResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_get_exercises_response(response_data, [function_create_exercise.response])
        validate_json_schema(instance=response.json(), schema=response_data.model_json_schema())
