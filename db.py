import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="13.233.192.85",
        user="sowmya",
        password="sowmya@1234",
        database="documentform"
    )