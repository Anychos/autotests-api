from pydantic import BaseModel, Field


class LoginRequestSchema(BaseModel):
    """
    Описание модели запроса на авторизацию
    """
    email: str
    password: str

class RefreshRequestSchema(BaseModel):
    """
    Описание модели запроса на обновление токена
    """
    refresh_token: str = Field(alias="refreshToken")

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
