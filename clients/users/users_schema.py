from pydantic import BaseModel, Field, EmailStr, constr, ConfigDict
from tools.data_generator import fake


class UserSchema(BaseModel):
    """
    Описание базовой модели пользователя
    """
    model_config = ConfigDict(populate_by_name=True) # позволяет обращаться к ключам модели по имени snake_case

    id: str
    email: EmailStr
    last_name: constr(min_length=1, max_length=50) = Field(alias="lastName")
    first_name: constr(min_length=1, max_length=50) = Field(alias="firstName")
    middle_name: constr(min_length=1, max_length=50) = Field(alias="middleName")

class GetUserResponseSchema(BaseModel):
    """
    Описание модели ответа на запрос получения пользователя
    """
    user: UserSchema

class CreateUserRequestSchema(BaseModel):
    """
    Описание модели запроса на создание пользователя
    """
    model_config = ConfigDict(populate_by_name=True)

    email: EmailStr = Field(default_factory=fake.email)
    password: constr(min_length=1, max_length=250) = Field(default_factory=fake.password)
    last_name: constr(min_length=1, max_length=50) = Field(alias="lastName", default_factory=fake.last_name)
    first_name: constr(min_length=1, max_length=50) = Field(alias="firstName", default_factory=fake.first_name)
    middle_name: constr(min_length=1, max_length=50) = Field(alias="middleName", default_factory=fake.middle_name)

class CreateUserResponseSchema(BaseModel):
    """
    Описание модели ответа на запрос создания пользователя
    """
    user: UserSchema

class UpdateUserRequestSchema(BaseModel):
    """
    Описание модели запроса на обновление пользователя
    """
    model_config = ConfigDict(populate_by_name=True)

    email: EmailStr | None = Field(default_factory=fake.email)
    last_name: constr(min_length=1, max_length=50) | None = Field(alias="lastName", default_factory=fake.last_name)
    first_name: constr(min_length=1, max_length=50) | None = Field(alias="firstName", default_factory=fake.first_name)
    middle_name: constr(min_length=1, max_length=50) | None = Field(alias="middleName", default_factory=fake.middle_name)

class UpdateUserResponseSchema(BaseModel):
    """
    Описание модели ответа на запрос обновления пользователя
    """
    user: UserSchema