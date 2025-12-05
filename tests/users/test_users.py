import pytest
from http import HTTPStatus

from clients.users.private_user_client import PrivateUserClient
from clients.users.public_user_client import PublicUserClient
from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema, GetUserResponseSchema
from fixtures.users import UserFixture
from tools.assertions.schema import validate_json_schema
from tools.assertions.users import assert_get_user_response
from tools.base_assertions import assert_status_code, assert_value
from tools.data_generator import fake


@pytest.mark.regression
@pytest.mark.smoke
@pytest.mark.users
class TestUser:
    @pytest.mark.parametrize('email', ['mail.ru', 'gmail.com', 'example.com'])
    def test_create_user(self, email: str, public_user_client: PublicUserClient):
        request = CreateUserRequestSchema(email=fake.email(email))

        response = public_user_client.create_user_api(request)

        response_data = CreateUserResponseSchema.model_validate_json(response.text)
        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_value(response_data.user.email, request.email, 'email')
        validate_json_schema(instance=response.json(), schema=response_data.model_json_schema())

    def test_get_user_me(self, function_create_user: UserFixture, private_user_client: PrivateUserClient):
        response = private_user_client.get_user_me_api()

        response_data = GetUserResponseSchema.model_validate_json(response.text)
        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_get_user_response(function_create_user.response, response_data)
        validate_json_schema(instance=response.json(), schema=response_data.model_json_schema())
