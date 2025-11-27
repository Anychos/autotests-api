import pytest
from pydantic import BaseModel

from clients.files.files_client import get_private_files_client, FilesClient
from clients.files.files_schema import CreateFileRequestSchema, CreateFileResponseSchema
from fixtures.users import UserFixture


class FileFixture(BaseModel):
    request: CreateFileRequestSchema
    response: CreateFileResponseSchema

@pytest.fixture
def files_client(function_create_user: UserFixture) -> FilesClient:
    return get_private_files_client(function_create_user.auth_user)

@pytest.fixture
def function_create_file(files_client: FilesClient) -> FileFixture:
    request = CreateFileRequestSchema(upload_file='./test_data/image.png')
    response = files_client.create_file(request)
    return FileFixture(request=request, response=response)