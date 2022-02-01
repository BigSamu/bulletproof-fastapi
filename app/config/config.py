import secrets

from pydantic import BaseSettings


class Settings(BaseSettings):

    # API URL PREFIX
    API_V1_STR: str = "/api/v1"
    
    # FAST API 
    TITLE: str = "Prducts and Sellers API"
    DESCRIPTION: str = " Get details for all the products on our website"
    TERMS_OF_SERVICE: str = "http://www.google.com"
    CONTACT: dict = {
        "Developer name": "Samuel Valdes Gutierrez",
        "website": "www.google.com",
        "email": "demo@gmail.com",
    }
    LICENSE_INFO: dict = {"name": "XYZ", "url": "http://www.gooogle.com"}

    # JWT TOKEN
    SECRET_KEY: str = secrets.token_urlsafe(32)
    ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES = 20 # in minutes


    # DATABASE
    SQLALCHEMY_DATABASE_URI: str = "sqlite:///./products_and_sellers.db"
    # SQLALCHEMY_DATABASE_URI: str = (
    #     "mysql+pymysql://root:root@127.0.0.1:3306/products_and_sellers"
    # )

    # class Config:
    #     env_file = ".env"


settings = Settings()
