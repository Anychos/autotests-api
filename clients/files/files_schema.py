from pydantic import BaseModel, Field, HttpUrl


class CreateFileRequestSchema(BaseModel):
    """
    Описание модели запроса на загрузку файла
    """
    filename: str = Field(default='image.png')
    directory: str = Field(default='courses')
    upload_file: str = Field(default='./test_data/image.png')

class FileSchema(BaseModel):
    """
    Описание базовой модели файла
    """
    id: str
    filename: str
    directory: str
    url: HttpUrl

class CreateFileResponseSchema(BaseModel):
    """
    Описание модели ответа на запрос загрузки файла
    """
    file: FileSchema

class GetFileResponseSchema(BaseModel):
    """
    Описание модели ответа на запрос получения файла
    """
    file: FileSchema