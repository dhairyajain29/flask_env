import mysql.connector
from mysql.connector import errorcode

# Database configuration
db_config = {
    'user': 'root',
    'password': 'root@123',
    'host': 'localhost',  
    'database': 'datamodel',
    'port': 3306
}

# Function to connect to the database
def get_db_connection():
    try:
        conn = mysql.connector.connect(**db_config)
        return conn
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print("Error:", err)
        return None
