import httpx
from tools.faker import get_random_email

# Создаем пользователя
create_user_payload = {
    "email": get_random_email(),
    "password": "password",
    "lastName": "Testov",
    "firstName": "Test",
    "middleName": "Testovich"
}
create_user_response = httpx.post("http://localhost:8000/api/v1/users", json=create_user_payload)
create_user_response_data = create_user_response.json()
print('Create user response:', create_user_response_data)
print('Status Code:', create_user_response.status_code)

# Инициализируем JSON-данные, которые будем отправлять в API
login_payload = {
    "email": create_user_payload["email"],
    "password": create_user_payload["password"]
}

# Выполняем запрос на аутентификацию
login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_payload)
login_response_data = login_response.json()

# Выводим полученный токен и статус код
print("Login response:", login_response_data)
print("Status Code:", login_response.status_code)

# Получаем данные пользователя
get_user_headers = {
    "Authorization": f"Bearer {login_response_data['token']['accessToken']}"
}
get_user_response = httpx.get(
    f"http://localhost:8000/api/v1/users/{create_user_response_data['user']['id']}",
    headers=get_user_headers
)
get_user_response_data = get_user_response.json()
print('Get user response:', get_user_response_data)
print('Status Code:', get_user_response.status_code)

# Удаляем пользователя
delete_user_headers = {
    "Authorization": f"Bearer {login_response_data['token']['accessToken']}"
}
delete_user_response = httpx.delete(
    f"http://localhost:8000/api/v1/users/{create_user_response_data['user']['id']}",
    headers=delete_user_headers
)
delete_user_response_data = delete_user_response.json()
print('Delete user data:', delete_user_response_data)
print('Status Code:', delete_user_response.status_code)