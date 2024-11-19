import mysql.connector

try:
    db = mysql.connector.connect(
        host="127.0.0.1",  # 또는 정확한 서버 IP
        user="readonly_user",
        password="12345678",
        database="crawled"
    )
    cursor = db.cursor()
    cursor.execute("SHOW TABLES;")
    for table in cursor:
        print(table)
    db.close()
except mysql.connector.Error as err:
    print(f"Error: {err}")