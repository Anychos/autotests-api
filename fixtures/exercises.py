import pytest
from pydantic import BaseModel

from clients.exercises.exercises_client import ExercisesClient, get_private_exercises_client
from clients.exercises.exercises_schema import CreateExerciseRequestSchema, CreateExerciseResponseSchema
from fixtures.courses import CoursesFixture
from fixtures.files import FileFixture
from fixtures.users import UserFixture


class ExercisesFixture(BaseModel):
        request: CreateExerciseRequestSchema
        response: CreateExerciseResponseSchema

@pytest.fixture
def exercises_client(function_create_user: UserFixture) -> ExercisesClient:
    return get_private_exercises_client(function_create_user.auth_user)

@pytest.fixture
def function_create_exercise(exercises_client: ExercisesClient,
                             function_create_user: UserFixture,
                             function_create_course: CoursesFixture,
                             function_create_file: FileFixture) -> ExercisesFixture:
    request = CreateExerciseRequestSchema()
    response = exercises_client.create_exercise(request)
    return ExercisesFixture(request=request, response=response)
