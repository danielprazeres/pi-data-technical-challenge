from fastapi import FastAPI
from app.routes import character_routes
from app.database.base import engine
from app.models import character

# Create database tables
character.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Character API",
    description="API for character management",
    version="1.0.0"
)

# Include routes
app.include_router(character_routes.router)

@app.get("/")
def read_root():
    """
    Root route that returns API information.
    """
    return {
        "message": "Welcome to Character API",
        "documentation": "/docs",
        "version": "1.0.0"
    } 