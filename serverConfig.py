from pyliteconf import Config as _Config
from os import getenv


class DatabaseConfig(_Config):
    _dialect = "mysql+asyncmy"

    _user = getenv("DB_USER")
    _password = getenv("DB_PASSWORD")
    _db_url = getenv("DB_URL")

    url = f"{_dialect}://{_user}:{_password}@{_db_url}"


class ElasticConfig(_Config):
    hosts = [getenv("ELASTIC_FULL_URL")]
