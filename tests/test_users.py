import jsonschema
import pytest
from clients.users.private_user_client import PrivateUserClient
from clients.users.public_user_client import PublicUserClient
from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema, GetUserResponseSchema
from http import HTTPStatus
from tools.assertions.users_assertions import assert_get_user_response
from tools.base_assertions import assert_status_code, assert_value
from tools.data_generator import fake


@pytest.mark.regression
@pytest.mark.users
@pytest.mark.parametrize('email', ['mail.ru', 'gmail.com', 'example.com'])
def test_create_user(email: str, public_user_client: PublicUserClient):
    email = fake.email(email)
    request = CreateUserRequestSchema(email=email)
    response = public_user_client.create_user_api(request)
    response_data = CreateUserResponseSchema.model_validate_json(response.text)
    assert_status_code(response.status_code, HTTPStatus.OK)
    assert_value(response_data.user.email, request.email, 'email')
    jsonschema.validate(instance=response.json(), schema=response_data.model_json_schema())

@pytest.mark.regression
@pytest.mark.users
def test_get_user_me(function_create_user, private_user_client: PrivateUserClient):
    response = private_user_client.get_user_me_api()
    assert_status_code(response.status_code, HTTPStatus.OK)
    response_data = GetUserResponseSchema.model_validate_json(response.text)
    assert_get_user_response(function_create_user.response, response_data)
    jsonschema.validate(instance=response.json(), schema=response_data.model_json_schema())
