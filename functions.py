import psycopg2
from sqlalchemy import create_engine, MetaData, Table, insert
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.ext.automap import automap_base
import os
from dotenv import load_dotenv

load_dotenv()

Base = declarative_base()
engine = create_engine(os.getenv("CONNECTION_STRING"))