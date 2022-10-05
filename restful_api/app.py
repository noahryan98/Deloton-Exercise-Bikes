import pandas as pd 
import json
import sqlalchemy
import snowflake.connector
from snowflake.sqlalchemy import URL
from sqlalchemy import create_engine
from flask import Flask, request
from dotenv import load_dotenv
import os

load_dotenv()

USER = os.environ.get('USER')
ACCOUNT = os.environ.get('ACCOUNT')
PASSWORD = os.environ.get('PASSWORD')
WAREHOUSE= os.environ.get('WAREHOUSE')
DATABASE= os.environ.get('DATABASE')
SCHEMA= os.environ.get('SCHEMA')


# SQLalchemy connection

engine = create_engine(URL(
    user=USER,
    password=PASSWORD,
    account=ACCOUNT,
    warehouse=WAREHOUSE,
    database=DATABASE,
    schema=SCHEMA
))

connection = engine.connect()


# Snowflake connection

conn = snowflake.connector.connect(
    user=USER,
    password=PASSWORD,
    account=ACCOUNT,
    warehouse=WAREHOUSE,
    database=DATABASE,
    schema=SCHEMA
)
cs = conn.cursor()


# API Endpoints