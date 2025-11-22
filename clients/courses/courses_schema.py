from pydantic import BaseModel, Field, ConfigDict
from clients.files.files_schema import FileSchema
from clients.users.users_schema import UserSchema


class CourseSchema(BaseModel):
    """
    Описание базовой модели курса
    """
    model_config = ConfigDict(populate_by_name=True)

    id: str
    title: str
    max_score: int = Field(default=None, alias='maxScore')
    min_score: int = Field(default=None, alias='minScore')
    description: str
    preview_file: FileSchema = Field(alias='previewFile')
    estimated_time: str = Field(default=None, alias='estimatedTime')
    created_by_user: UserSchema = Field(alias='createdByUser')

class GetCourseByUserRequestSchema(BaseModel):
    """
    Описание модели запроса на получение курсов пользователя
    """
    model_config = ConfigDict(populate_by_name=True)

    user_id: str = Field(alias='userId')

class GetCourseByUserResponseSchema(BaseModel):
    """
    Описание модели ответа на получение курсов пользователя
    """
    courses: list[CourseSchema]

class GetCourseByIdRequestSchema(BaseModel):
    """
    Описание модели запроса на получение курса по id
    """
    course_id: str

class GetCourseByIdResponseSchema(BaseModel):
    """
    Описание модели ответа на получение курса по id
    """
    course: CourseSchema

class CreateCourseRequestSchema(BaseModel):
    """
    Описание модели запроса на создание курса
    """
    model_config = ConfigDict(populate_by_name=True)

    title: str
    max_score: int = Field(default=None, alias='maxScore')
    min_score: int = Field(default=None, alias='minScore')
    description: str
    estimated_time: str = Field(default=None, alias='estimatedTime')
    preview_file_id: str = Field(alias='previewFileId')
    created_by_user_id: str = Field(alias='createdByUserId')

class CreateCourseResponseSchema(BaseModel):
    """
    Описание модели ответа на создание курса
    """
    course: CourseSchema

class UpdateCourseRequestSchema(BaseModel):
    """
    Описание модели запроса на обновление курса
    """
    model_config = ConfigDict(populate_by_name=True)

    title: str | None
    max_score: int = Field(default=None, alias='maxScore')
    min_score: int = Field(default=None, alias='minScore')
    description: str | None
    estimated_time: str = Field(default=None, alias='estimatedTime')

class UpdateCourseResponseSchema(BaseModel):
    """
    Описание модели ответа на обновление курса
    """
    course: CourseSchema



