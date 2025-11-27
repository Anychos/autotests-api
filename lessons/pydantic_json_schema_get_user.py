import jsonschema
from clients.private_builder import AuthUserSchema
from clients.users.private_user_client import get_private_user_client
from clients.users.public_user_client import get_public_user_client
from clients.users.users_schema import CreateUserRequestSchema, GetUserResponseSchema
from tools.data_generator import fake


public_user_client = get_public_user_client()
create_user_request = CreateUserRequestSchema(
    email=fake.email(),
    password=fake.password(),
    last_name=fake.last_name(),
    first_name=fake.first_name(),
    middle_name=fake.middle_name()
)
create_user_response = public_user_client.create_user(create_user_request)
print(create_user_response)

auth_user_data = AuthUserSchema(
    email=create_user_request.email,
    password=create_user_request.password
)
private_user_client = get_private_user_client(auth_user_data)
get_user_response = private_user_client.get_user_by_id_api(create_user_response.user.id)
print(get_user_response.json())
get_user_response_schema = GetUserResponseSchema.model_json_schema() # Генерируем JSON-схему для ожидаемого ответа
print(get_user_response_schema)
jsonschema.validate(instance=get_user_response.json(), schema=get_user_response_schema) # Проверяем соответствие JSON-ответа схеме