from http import HTTPStatus
import jsonschema
import pytest
from clients.auth.auth_client import get_auth_client
from clients.auth.auth_schema import LoginRequestSchema, LoginResponseSchema
from clients.users.public_user_client import get_public_user_client
from clients.users.users_schema import CreateUserRequestSchema
from tools.assertions.auth_assertions import assert_login_response
from tools.base_assertions import assert_status_code


@pytest.mark.regression
@pytest.mark.authentication
def test_login():
    user_client = get_public_user_client()
    auth_client = get_auth_client()

    create_user_request = CreateUserRequestSchema()
    create_user_response = user_client.create_user(create_user_request)
    print(create_user_response)

    login_request = LoginRequestSchema(
        email=create_user_request.email,
        password=create_user_request.password
    )
    login_response = auth_client.login_api(login_request)
    login_response_data = LoginResponseSchema.model_validate_json(login_response.text)

    assert_status_code(login_response.status_code, HTTPStatus.OK)
    assert_login_response(login_response_data)
    jsonschema.validate(instance=login_response.json(), schema=login_response_data.model_json_schema())


