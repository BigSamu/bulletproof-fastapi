import uvicorn

from fastapi import FastAPI
from .api.v1 import api_router
from .config.config import settings

# *******************************************************************************
# FASTAPI APP SETTINGS
# *******************************************************************************

app = FastAPI(
    title=settings.TITLE,
    description=settings.DESCRIPTION,
    terms_of_service=settings.TERMS_OF_SERVICE,
    contact=settings.CONTACT,
    license_info=settings.LICENSE_INFO)


app.include_router(api_router, prefix=settings.API_V1_STR)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
