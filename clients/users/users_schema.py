from pydantic import BaseModel, Field, EmailStr, constr, ConfigDict


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

class GerUserResponseSchema(BaseModel):
    """
    Описание модели ответа на запрос получения пользователя
    """
    user: UserSchema

class CreateUserRequestSchema(BaseModel):
    """
    Описание модели запроса на создание пользователя
    """
    model_config = ConfigDict(populate_by_name=True)

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

class UpdateUserRequestSchema(BaseModel):
    """
    Описание модели запроса на обновление пользователя
    """
    model_config = ConfigDict(populate_by_name=True)

    email: EmailStr
    last_name: constr(min_length=1, max_length=50) = Field(default=None, alias="lastName")
    first_name: constr(min_length=1, max_length=50) = Field(default=None, alias="firstName")
    middle_name: constr(min_length=1, max_length=50) = Field(default=None, alias="middleName")

class UpdateUserResponseSchema(BaseModel):
    """
    Описание модели ответа на запрос обновления пользователя
    """
    user: UserSchema