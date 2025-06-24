import httpx
from tools import faker

"""Create user"""
create_user_payload = {
    "email": faker.get_random_email(),
    "password": "password",
    "lastName": "Testov",
    "firstName": "Test",
    "middleName": "Testovich"
}

create_user_response = httpx.post("http://localhost:8000/api/v1/users", json=create_user_payload)
create_user_data = create_user_response.json()
print("User created")
print('Create user response:', create_user_data)
print('Status Code:', create_user_response.status_code)

"""Login user"""
login_payload = {
    "email": create_user_payload["email"],
    "password": create_user_payload["password"]
}

login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_payload)
login_response_data = login_response.json()
print("Login successful")
print("Login response:", login_response_data)
print("Status Code:", login_response.status_code)

"""Update user"""
update_user_payload = {
    "email": faker.get_random_email(),
    "lastName": "Popov",
    "firstName": "Anton",
    "middleName": "Ershov"

}

update_user_headers = {
    "Authorization": f"Bearer {login_response_data['token']['accessToken']}"
}
update_user_response = httpx.patch(
    f"http://localhost:8000/api/v1/users/{create_user_data['user']['id']}", headers=update_user_headers,
    json=update_user_payload)
update_user_data = update_user_response.json()
print("User updated")
print('Update user response:', update_user_data)
print('Status Code:', update_user_response.status_code)