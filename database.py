# DB ga ulanish
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

URL_DATABASE = "postgresql://postgres:root@localhost:5432/pythonlesson"

# DB ulanish va uni monitor qilish
engine = create_engine (URL_DATABASE)

# har bir so'rov uchun alohida bazaga ulanish session
SessionLocal = sessionmaker (autocommit = False ,autoflush=False , bind=engine)

# Bazadagi jadvallar uchun
Base = declarative_base()

