from clients.private_builder import AuthUserSchema
from clients.users.private_user_client import get_private_user_client
from clients.users.public_user_client import get_public_user_client
from clients.users.users_schema import CreateUserRequestSchema
from tools.test_data_generator import fake


public_user_client = get_public_user_client()
create_user_request_body = CreateUserRequestSchema(
    email=fake.email(),
    password=fake.password(),
    last_name=fake.last_name(),
    first_name=fake.first_name(),
    middle_name=fake.middle_name()
)
create_user_response = public_user_client.create_user(create_user_request_body)
print(create_user_response)

auth_user_dict = AuthUserSchema(
    email=create_user_request_body.email,
    password=create_user_request_body.password
)
private_user_client = get_private_user_client(auth_user_dict)
get_user_response = private_user_client.get_user_by_id(create_user_response.user.id)
print(get_user_response)