import ujson
from pydantic import BaseConfig, BaseSettings, BaseModel, PostgresDsn, SecretStr, PositiveInt, Field


class Config(BaseConfig):
    json_dumps = ujson.dumps
    json_loads = ujson.loads
    orm_mode = True


class Schema(BaseModel):
    Config = Config


class Settings(BaseSettings):
    DATABASE_URL: PostgresDsn
    SECRET_KEY: SecretStr
    EXPIRE_JWT: PositiveInt
    ALGORITHM: str = Field(default='HS256')

    class Config:
        env_file = '.env'
