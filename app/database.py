import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.logger import logger
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise ValueError("DATABASE_URL is not set in the environment variables")

engine = create_engine(DATABASE_URL)


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def init_db():
    """
    Inicializa la base de datos creando todas las tablas definidas en los modelos.
    """
    try:
        Base.metadata.create_all(bind=engine)
        logger.debug("Base de datos inicializada correctamente.")
    except Exception as e:
        logger.error(f"Error al inicializar la base de datos: {e}")


def get_db():

    try:
        db: Session = SessionLocal()
        logger.debug("Database session created successfully!")  # Log per depuració
        yield db
    except HTTPException as http_exc:

        raise http_exc
    except Exception as e:
        logger.debug(f"Error during database connection: {type(e).__name__}, {e}")
        raise HTTPException(status_code=500, detail="Database connection error")
    finally:
        try:
            db.close()
            logger.debug("Database session closed")  # Log per depuració
        except Exception as close_err:
            logger.debug(f"Error while closing database session: {type(close_err).__name__}, {close_err}")

def reset_database():

    logger.debug("Esborrant les taules existents...")
    Base.metadata.drop_all(bind=engine)  # Esborra totes les taules
    logger.debug("Creant les taules de nou...")
    Base.metadata.create_all(bind=engine)  # Re-crea totes les taules
    logger.debug("Base de dades reinicialitzada correctament.")


if __name__ == "__main__":
    reset_database()