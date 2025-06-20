# init_db.py (will be compiled later)
import pymysql
import os
from dotenv import load_dotenv
import time

schema = """
create database if not exists luxiva_ecommerce;

use luxiva_ecommerce;

create table product_items(
id INT auto_increment NOT NULL primary key,
name varchar(30),
discription text,
price int,
quantaty int,
rating int);

insert into product_items (name, discription, price, quantaty) values (
"POLO","Cotton round-neck t-shirt for daily wear.", 5000, 20);
"""

def wait_for_db():
    for _ in range(10):
        try:
            conn = pymysql.connect(host=os.getenv("DB_HOST"), user=os.getenv("DB_USER"), password=os.getenv("DB_PASSWORD"), database=os.getenv("DB_NAME"), cursorclass=pymysql.cursors.DictCursor)
            return conn
        except:
            print("Waiting for MySQL to be ready...")
            time.sleep(2)
    raise Exception("MySQL not reachable")


def initialize_database():
    conn = wait_for_db()
    cursor = conn.cursor()
    for stmt in schema.strip().split(';'):
        if stmt.strip():
            cursor.execute(stmt)
    conn.commit()
    cursor.close()
    conn.close()

if __name__ == "__main__":
    initialize_database()
