from db import get_connection

def verify_admin(username: str, password: str):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    query = "SELECT * FROM adminlogin WHERE email = %s AND password = %s"
    cursor.execute(query, (username, password))
    admin = cursor.fetchone()
    cursor.close()
    conn.close()
    return admin

def get_user_tasks():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    query = "SELECT * FROM user_task"
    cursor.execute(query)
    tasks = cursor.fetchall()
    cursor.close()
    conn.close()
    return tasks

