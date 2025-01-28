from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
from app.routes import auth_routes
from app.database import init_db
from app.logger import logger


app = FastAPI(
    title="MLB SCOUT AI API",
    description="",
    version="1.0",
    docs_url="/docs",
    redoc_url="/redoc",
)

init_db()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

# Registrar rutes
app.include_router(auth_routes.router, prefix="/auth", tags=["Authentication"])




