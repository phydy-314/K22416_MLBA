from Salemanagement.libs.connector import MySQLConnector
from Salemanagement.models.nhanvien import NhanVien


class NhanVienConnector(MySQLConnector):
    def dang_nhap(self,username,password):
        cursor = self.conn.cursor()
        sql= "select * from nhanvien where username=%s and password=%s"
        val = (username,password)
        cursor.execute(sql,val)
        dataset = cursor.fetchone()
        nv = None
        if dataset != None:
            id, manhanvien, tennhanvien, username, password, isdeleted = dataset
            nv = NhanVien(id,manhanvien,tennhanvien,username,password,isdeleted)
        cursor.close()
        return nv