from uuid import UUID, uuid4
from pydantic import BaseModel, Field, EmailStr, constr


class UserSchema(BaseModel):
    """
    Описание базовой модели пользователя
    """
    model_config = {
        "populate_by_name": True
    }

    id: UUID = Field(default_factory=uuid4)
    email: EmailStr
    last_name: constr(min_length=1, max_length=50) = Field(alias="lastName")
    first_name: constr(min_length=1, max_length=50) = Field(alias="firstName")
    middle_name: constr(min_length=1, max_length=50) = Field(alias="middleName")

class CreateUserRequestSchema(BaseModel):
    """
    Описание модели запроса на создание пользователя
    """
    model_config = {
        "populate_by_name": True
    }

    email: EmailStr
    password: constr(min_length=1, max_length=250)
    last_name: constr(min_length=1, max_length=50) = Field(alias="lastName")
    first_name: constr(min_length=1, max_length=50) = Field(alias="firstName")
    middle_name: constr(min_length=1, max_length=50) = Field(alias="middleName")

class CreateUserResponseSchema(BaseModel):
    """
    Описание модели ответа на запрос создания пользователя
    """
    user: UserSchema