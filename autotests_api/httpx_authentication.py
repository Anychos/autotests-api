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

# payload для обновления токена
refresh_payload = {
    "refreshToken": login_response_data["token"]["refreshToken"]
}

# Выполняем запрос на обновление токена
refresh_response = httpx.post("http://localhost:8000/api/v1/authentication/refresh", json=refresh_payload)
refresh_response_data = refresh_response.json()

# Выводим обновленные токены
print("Refresh response:", refresh_response_data)
print("Status Code:", refresh_response.status_code)