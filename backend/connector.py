import pymysql
import pymysql.cursors
import os
from dotenv import load_dotenv

from pathlib import Path
load_dotenv(dotenv_path=Path("/app/.env"))

def connection():
    try:
        connector = pymysql.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME"),
            port=int(os.getenv("DB_PORT")),
            cursorclass=pymysql.cursors.DictCursor
        )
        return connector
    except Exception as e:
        raise Exception("Error in database connection") from e
