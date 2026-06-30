from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///./grades.db"

engine =create_engine(DATABASE_URL, connect_args={"check_same_thread" : False})

# sessionlocal is a class that will be used to create database sessions
# autocommit=False means that the session will not automatically commit changes to the database
# autoflush=False means that the session will not automatically flush changes to the database
# bind=engine means that the session will be bound to the engine created above
SessionLocal =sessionmaker(autoflush=False, autocommit=False, bind=engine)

# Base is a class that will be used to create database models
Base = declarative_base()

def get_db():
    db = SessionLocal() # creates a fresh/new database session
    try:  # starts a try block to ensure that the database session is closed after use
        yield db # yields the database session to the caller
    finally: # ensures that the database session is closed after use
        db.close()