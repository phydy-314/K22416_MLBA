import mysql.connector
class MySQLConnector:
    def __init__(self,server=None, port=None, database=None,
                 username=None,password=None):
        if server == None:
            self.server = 'localhost'
            self.port = 3306
            self.database = 'k22416c_sales'
            self.username = 'root'
            self.password = '123456'
        else:
            self.server = server
            self.port = port
            self.database = database
            self.username = username
            self.password = password
    def connect(self):
        self.conn = mysql.connector.connect(
            host = self.server,
            port = self.port,
            database = self.database,
            user = self.username,
            password = self.password
        )
        return self.conn


# from mysql.connector import Error
#
# # Import lớp MySQLConnector đã viết
# from Salemanagement.libs.connector import MySQLConnector
#
#
# def test_mysql_connection():
#     try:
#         # Khởi tạo đối tượng kết nối
#         db = MySQLConnector()
#         conn = db.connect()
#
#         if conn.is_connected():
#             print("✅ Kết nối MySQL thành công!")
#
#             # Tạo con trỏ để thực hiện truy vấn
#             cursor = conn.cursor()
#
#             # Kiểm tra truy vấn: Lấy danh sách nhân viên
#             query = "SELECT * FROM nhanvien LIMIT 5;"
#             cursor.execute(query)
#
#             # Lấy dữ liệu truy vấn
#             rows = cursor.fetchall()
#
#             # Kiểm tra nếu có dữ liệu
#             if rows:
#                 print("🔹 Kết quả truy vấn:")
#                 for row in rows:
#                     print(row)
#             else:
#                 print("⚠️ Truy vấn thành công nhưng không có dữ liệu.")
#
#             # Đóng con trỏ và kết nối
#             cursor.close()
#             conn.close()
#             print("🔒 Đã đóng kết nối MySQL.")
#
#         else:
#             print("❌ Kết nối MySQL thất bại!")
#
#     except Error as e:
#         print(f"❌ Lỗi MySQL: {e}")
#
#
# # Chạy kiểm tra kết nối và truy vấn
# test_mysql_connection()
#
# def test_login(username, password):
#     try:
#         db = MySQLConnector()
#         conn = db.connect()
#         cursor = conn.cursor()
#
#         # Thực hiện truy vấn đăng nhập
#         sql = "SELECT * FROM nhanvien WHERE username=%s AND password=%s"
#         val = (username, password)
#         cursor.execute(sql, val)
#         user = cursor.fetchone()
#
#         if user:
#             print("✅ Đăng nhập thành công!", user)
#         else:
#             print("❌ Đăng nhập thất bại! Kiểm tra lại username/password.")
#
#         cursor.close()
#         conn.close()
#     except Exception as e:
#         print(f"❌ Lỗi: {e}")
#
# # Kiểm tra với tài khoản trong database
# test_login("teoteo", "123")  # Thay bằng username & password có trong DB
# test_login("hodo", "456")
# test_login("hehe", "789")
