from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.constants.common import (
    API_TITLE,
    API_VERSION,
    API_DESCRIPTION,
)
from src.routers.google_meet_routes import google_meet_router
# END IMPORTS


# APP CONFIG
app = FastAPI(title=API_TITLE, description=API_DESCRIPTION,
              version=API_VERSION)

origins = ['*']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ROUTERS
app.include_router(google_meet_router)
