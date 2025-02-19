from flask import Flask
from flask_mysqldb import MySQL

app = Flask(__name__)

# MySQL configurations
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '123456'
app.config['MYSQL_DB'] = 'studentmanagement'
app.config['MYSQL_HOST'] = 'localhost'

mysql = MySQL(app)

try:
    # Tạo ngữ cảnh ứng dụng để kết nối MySQL
    with app.app_context():
        conn = mysql.connection
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM student")
        data = cursor.fetchall()
        print("ID\tCode\tName")
        for item in data:
            print(item[0], "\t", item[1], "\t", item[2])

        cursor.close()  # Đóng con trỏ sau khi truy vấn

except Exception as e:
    print("Error: ", e)

finally:
    print("Execution complete")
