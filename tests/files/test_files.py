from http import HTTPStatus
import pytest

from clients.error_schema import ValidationErrorResponseSchema, InternalErrorResponseSchema
from clients.files.files_client import FilesClient
from clients.files.files_schema import CreateFileRequestSchema, CreateFileResponseSchema, GetFileResponseSchema
from fixtures.files import FileFixture
from tools.assertions.files import assert_create_file_response, assert_get_file_response, \
    assert_create_file_with_empty_filename_response, assert_create_file_with_empty_directory_response, \
    assert_file_not_found_response, assert_get_file_with_incorrect_file_id_response
from tools.assertions.schema import validate_json_schema
from tools.base_assertions import assert_status_code


@pytest.mark.files
@pytest.mark.regression
@pytest.mark.smoke
@pytest.mark.positive
class TestFilesPositive:
    def test_create_file(self, files_client: FilesClient):
        request = CreateFileRequestSchema()

        response = files_client.create_file_api(request)
        response_data = CreateFileResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        validate_json_schema(instance=response.json(), schema=response_data.model_json_schema())
        assert_create_file_response(request, response_data)

    def test_get_file(self, function_create_file: FileFixture, files_client: FilesClient):
        response = files_client.get_file_api(function_create_file.response.file.id)
        response_data = GetFileResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        validate_json_schema(instance=response.json(), schema=response_data.model_json_schema())
        assert_get_file_response(response_data, function_create_file.response)

@pytest.mark.files
@pytest.mark.regression
@pytest.mark.negative
class TestFilesNegative:
    def test_create_file_without_filename(self, files_client: FilesClient):
        request = CreateFileRequestSchema(filename='')

        response = files_client.create_file_api(request)
        response_data = ValidationErrorResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.UNPROCESSABLE_ENTITY)
        assert_create_file_with_empty_filename_response(response_data)
        validate_json_schema(instance=response.json(), schema=response_data.model_json_schema())

    def test_create_file_without_directory(self, files_client: FilesClient):
        request = CreateFileRequestSchema(directory='')

        response = files_client.create_file_api(request)
        response_data = ValidationErrorResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.UNPROCESSABLE_ENTITY)
        assert_create_file_with_empty_directory_response(response_data)
        validate_json_schema(instance=response.json(), schema=response_data.model_json_schema())

    def test_delete_file(self, files_client: FilesClient, function_create_file: FileFixture):
        delete_response = files_client.delete_file_api(function_create_file.response.file.id)

        assert_status_code(delete_response.status_code, HTTPStatus.OK)

        get_response = files_client.get_file_api(function_create_file.response.file.id)
        get_response_data = InternalErrorResponseSchema.model_validate_json(get_response.text)

        assert_status_code(get_response.status_code, HTTPStatus.NOT_FOUND)
        assert_file_not_found_response(get_response_data)
        validate_json_schema(get_response.json(), get_response_data.model_json_schema())

    def test_get_file_with_incorrect_file_id(self, files_client: FilesClient):
        response = files_client.get_file_api(file_id="incorrect-file-id")
        response_data = ValidationErrorResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.UNPROCESSABLE_ENTITY)
        assert_get_file_with_incorrect_file_id_response(response_data)
        validate_json_schema(instance=response.json(), schema=response_data.model_json_schema())