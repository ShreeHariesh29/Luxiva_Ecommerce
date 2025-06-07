import pymysql
import pymysql.cursors


def connection():
    try:
        connector = pymysql.connect(
            host= "host.docker.internal",
            user= "root",
            password= "1234",
            database= "newecommerce",
            port= 3306,
            cursorclass = pymysql.cursors.DictCursor
        )
        return connector
    except Exception as e :
        raise Exception("Error in database connection") from e
    