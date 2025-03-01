import mysql.connector
from mysql.connector import Error
from flask import Flask

app = Flask(__name__)

@app.route('/')
def check_mysql_connection():
    try:
        connection = mysql.connector.connect(
            host='eptest-server.mysql.database.azure.com',
            user='imhryoibrc',
            password='octZaEIfT$QwHu$$',
            database='eptest-database'
        )
        if connection.is_connected():
            return "Connection to MySQL database was successful!"
    except Error as e:
        return f"Error while connecting to MySQL: {e}"
    finally:
        if connection.is_connected():
            connection.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)