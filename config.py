from pydantic import BaseModel, FilePath, HttpUrl
from pydantic_settings import BaseSettings, SettingsConfigDict


class HTTPClientSettings(BaseModel):
    base_url: HttpUrl
    timeout: float = 10.0

    @property
    def url(self) -> str:
        return str(self.base_url)

class TestDataSettings(BaseModel):
    image_png_file: FilePath

class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        env_nested_delimiter='.'
    )

    test_data: TestDataSettings
    http_client: HTTPClientSettings

settings = Settings()

