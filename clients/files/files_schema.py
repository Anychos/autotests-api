from pydantic import BaseModel, HttpUrl


class CreateFileRequestSchema(BaseModel):
    """
    Описание модели запроса на загрузку файла
    """
    filename: str
    directory: str
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