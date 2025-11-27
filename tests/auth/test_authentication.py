from http import HTTPStatus
import jsonschema
import pytest

from clients.auth.auth_client import AuthClient
from clients.auth.auth_schema import LoginRequestSchema, LoginResponseSchema
from fixtures.users import UserFixture
from tools.assertions.auth_assertions import assert_login_response
from tools.base_assertions import assert_status_code


@pytest.mark.regression
@pytest.mark.authentication
class TestAuthentication:
    def test_login(self,
            function_create_user: UserFixture,
            auth_client: AuthClient
    ):
        login_request = LoginRequestSchema(
            email=function_create_user.email,
            password=function_create_user.password
        )
        login_response = auth_client.login_api(login_request)
        login_response_data = LoginResponseSchema.model_validate_json(login_response.text)

        assert_status_code(login_response.status_code, HTTPStatus.OK)
        assert_login_response(login_response_data)
        jsonschema.validate(instance=login_response.json(), schema=login_response_data.model_json_schema())


