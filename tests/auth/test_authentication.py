from http import HTTPStatus
import pytest

from tools.assertions.schema import validate_json_schema

from clients.auth.auth_client import AuthClient
from clients.auth.auth_schema import LoginRequestSchema, LoginResponseSchema
from fixtures.users import UserFixture
from tools.assertions.auth import assert_login_response
from tools.base_assertions import assert_status_code


@pytest.mark.regression
@pytest.mark.smoke
@pytest.mark.authentication
class TestAuthentication:
    def test_login(self,
            function_create_user: UserFixture,
            auth_client: AuthClient
    ):

        request = LoginRequestSchema(
            email=function_create_user.email,
            password=function_create_user.password
        )

        response = auth_client.login_api(request)
        response_data = LoginResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_login_response(response_data)
        validate_json_schema(instance=response.json(), schema=response_data.model_json_schema())


