from clients.private_builder import AuthUserDict
from clients.users.private_user_client import get_private_user_client
from clients.users.public_user_client import get_public_user_client, CreateUserRequestBody


email = 'test31@mail.ru'


public_user_client = get_public_user_client()
create_user_request_body = CreateUserRequestBody(
    email=email,
    password='password',
    lastName='lastName',
    firstName='firstName',
    middleName='middleName'
)
create_user_response = public_user_client.create_user(create_user_request_body)
print(create_user_response)


auth_user_Dict = AuthUserDict(
    email=email,
    password='password'
)
private_user_client = get_private_user_client(auth_user_Dict)
get_user_response = private_user_client.get_user_by_id(create_user_response['user']['id'])
print(get_user_response)