import secrets

from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    # API URL PREFIX
    API_V1_STR: str = "/api/v1"
    
    # FAST API 
    TITLE: str = "FastAPI Bulletproof"
    DESCRIPTION: str = "A simple FastAPI boilerplate with an example of product and sellers"
    TERMS_OF_SERVICE: str = "http://www.google.com"
    CONTACT: dict = {
        "Developer name": "Samuel Valdes Gutierrez",
        "website": "www.bigsamu.com",
        "email": "demo@gmail.com",
    }
    LICENSE_INFO: dict = {"name": "XYZ", "url": "http://www.gooogle.com"}

    # JWT TOKEN
    SECRET_KEY: str = secrets.token_urlsafe(32)
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 20 # in minutes


    # DATABASE
    SQLALCHEMY_DATABASE_URI: str = "sqlite:///./products_and_sellers.db"
    # SQLALCHEMY_DATABASE_URI: str = (
    #     "mysql+pymysql://root:root@127.0.0.1:3306/products_and_sellers"
    # )

    # class Config:
    #     env_file = ".env"


settings = Settings()
