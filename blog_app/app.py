from email.mime import application
from fastapi import FastAPI
from .router.api import router
from .router import models
from .router.database import engine

models.Base.metadata.create_all(bind=engine)


def get_application():
    application = FastAPI()
    application.include_router(router)
    return application


