from pyliteconf import Config as _Config


class DatabaseConfig(_Config):
    _dialect = "mysql+asyncmy"

    _user = "USER_NAME_STRING"
    _password = "USER_PASS_STRING"
    _db_url = "URL_STRING_ip:port/path/to/database"
    #                   OR
    # _user = getenv("DB_USER")
    # _password = getenv("DB_USER_PASS")
    # _db_url = getenv("DB_USER_URL")

    url = f"{_dialect}://{_user}:{_password}@{_db_url}"


class ElasticConfig(_Config):
    hosts = ["your_url"]
