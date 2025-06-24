import httpx  # Импортируем библиотеку HTTPX

# Инициализируем JSON-данные, которые будем отправлять в API
login_payload = {
    "email": "test@mail.ru",
    "password": "password"
}

# Выполняем запрос на аутентификацию
login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_payload)
login_response_data = login_response.json()

# Выводим полученный токен и статус код
print("Login response:", login_response_data)
print("Status Code:", login_response.status_code)

users_me_response = httpx.get("http://localhost:8000/api/v1/users/me", headers={"Authorization": f"Bearer {login_response_data['token']['accessToken']}"})
users_me_response_data = users_me_response.json()

# Выводим полученный json ответ и статус код
print("/api/v1/users/me response:", users_me_response_data)
print("Status Code:", users_me_response.status_code)