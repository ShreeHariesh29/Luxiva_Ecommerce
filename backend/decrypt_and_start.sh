#!/bin/sh

# Wait for MySQL using pure Python
python3 -c "
import time
import pymysql

while True:
    try:
        conn = pymysql.connect(
            host='db', user='root', password='1234', database='newecommerce', port=3306
        )
        conn.close()
        print('MySQL is ready.')
        break
    except Exception as e:
        print('Waiting for MySQL...', str(e))
        time.sleep(2)
"

# Run decrypted SQL directly in memory
python3 -c "
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import pymysql

key = b'ThisIsASecretKey'
iv = b'ThisIsAnIV123456'

with open('/encrypted.sql', 'rb') as f:
    ct = f.read()

cipher = AES.new(key, AES.MODE_CBC, iv)
sql = unpad(cipher.decrypt(ct), AES.block_size).decode()

conn = pymysql.connect(
    host='db',
    user='root',
    password='1234',
    database='newecommerce',
    port=3306,
    cursorclass=pymysql.cursors.DictCursor
)

cursor = conn.cursor()
for stmt in sql.split(';'):
    if stmt.strip():
        cursor.execute(stmt)

conn.commit()
cursor.close()
conn.close()
print('Decrypted SQL executed successfully.')
"

# Start backend
python3 main.pyc
