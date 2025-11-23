from pydantic import BaseModel, Field
from tools.test_data_generator import fake


class LoginRequestSchema(BaseModel):
    """
    Описание модели запроса на авторизацию
    """
    email: str = Field(default_factory=fake.email) # генерация случайного email
    password: str = Field(default_factory=fake.password)

class RefreshRequestSchema(BaseModel):
    """
    Описание модели запроса на обновление токена
    """
    refresh_token: str = Field(alias="refreshToken", default_factory=fake.description)

class TokenSchema(BaseModel):
    """
    Описание модели токена
    """
    token_type: str = Field(alias="tokenType")
    access_token: str = Field(alias="accessToken")
    refresh_token: str = Field(alias="refreshToken")

class LoginResponseSchema(BaseModel):
    """
    Описание модели ответа запроса на авторизацию
    """
    token: TokenSchema
