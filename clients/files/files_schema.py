from pydantic import BaseModel, HttpUrl, Field
from tools.test_data_generator import fake


class CreateFileRequestSchema(BaseModel):
    """
    Описание модели запроса на загрузку файла
    """
    filename: str = Field(default='image.png')
    directory: str = Field(default='courses')
    upload_file: str

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