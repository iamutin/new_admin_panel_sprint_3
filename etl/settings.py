from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class PostgresSettings(BaseSettings):
    model_config = SettingsConfigDict(env_prefix='postgres_')
    host: str = Field(..., alias='SQL_HOST')
    port: int = Field(..., alias='SQL_PORT')
    dbname: str = Field(..., alias='POSTGRES_DB')
    user: str = ...
    password: str = ...

    def get_dsl(self):
        return self.model_dump()


class ElasticsearchSettings(BaseSettings):
    model_config = SettingsConfigDict(env_prefix='es_')
    host: str = ...
    port: str = ...

    def get_url(self):
        return f'http://{self.host}:{self.port}'


pg_settings = PostgresSettings()
es_settings = ElasticsearchSettings()
