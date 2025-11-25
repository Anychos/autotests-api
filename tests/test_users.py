import jsonschema
import pytest
from clients.users.public_user_client import get_public_user_client
from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema
from http import HTTPStatus
from tools.base_assertions import assert_status_code, assert_value


@pytest.mark.regression
@pytest.mark.users
def test_create_user():
    public_user_client = get_public_user_client()
    create_user_request = CreateUserRequestSchema()
    create_user_response = public_user_client.create_user_api(create_user_request)
    create_user_response_data = CreateUserResponseSchema.model_validate_json(create_user_response.text)
    assert_status_code(create_user_response.status_code, HTTPStatus.OK)
    assert_value(create_user_response_data.user.email, create_user_request.email, 'email')
    jsonschema.validate(instance=create_user_response.json(), schema=create_user_response_data.model_json_schema())