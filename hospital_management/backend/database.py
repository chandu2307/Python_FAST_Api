"""
    Source Code for database connection
"""
import os
import logging
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import (
    sessionmaker ,
    declarative_base
)

logging.basicConfig(level=logging.INFO)

load_dotenv()

DB_HOST = os.getenv("DB_HOST")
DB_PORT = int(os.getenv("DB_PORT"))
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")

DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

logging.info("Establishing Engine...")
engine = create_engine(DATABASE_URL)

logging.info("Establishing Session...")
SessionLocal = sessionmaker(
                    autocommit = False,
                    autoflush = False,
                    bind = engine 
                )

Base = declarative_base()
