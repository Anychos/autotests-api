import httpx

# Инициализируем клиент
client = httpx.Client(base_url="http://localhost:8000/api/v1",
                      timeout=25,
                      headers={"Authorization": f"Bearer {login_response_data['token']['accessToken']}"})

# Выполняем GET-запрос, используя клиент
response = client.get("/me")

# Выводим ответ в консоль
print(response.text)