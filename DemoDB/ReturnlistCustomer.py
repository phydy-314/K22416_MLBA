import sqlite3
import pandas as pd

def fetch_customers_with_minimum_invoices(database_file, minimum_invoices):
    connection = None
    try:
        # Kết nối tới cơ sở dữ liệu
        connection = sqlite3.connect(database_file)
        query = f"""
        SELECT 
            Customer.CustomerId, 
            Customer.FirstName || ' ' || Customer.LastName AS FullName,
            COUNT(Invoice.InvoiceId) AS TotalInvoices
        FROM Customer
        JOIN Invoice ON Customer.CustomerId = Invoice.CustomerId
        GROUP BY Customer.CustomerId
        HAVING COUNT(Invoice.InvoiceId) >= {minimum_invoices};
        """
        # Thực thi câu truy vấn và chuyển kết quả sang DataFrame
        result = pd.read_sql_query(query, connection)
        return result

    except sqlite3.Error as e:
        print('Lỗi xảy ra -', e)
        return None

    finally:
        if connection:
            connection.close()

# Sử dụng hàm
db_file_path = '../databases/Chinook_Sqlite.sqlite'
min_invoices_required = 6
customers_df = fetch_customers_with_minimum_invoices(db_file_path, min_invoices_required)

if customers_df is not None:
    print(customers_df)
