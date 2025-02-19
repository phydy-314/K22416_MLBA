from Salemanagement.libs.sanphamconnector import SanPhamConnector

spc = SanPhamConnector()
spc.connect()
dssp = spc.LaySanPhamTheoMaDanhMuc(1)
print("DSsp co ma danh muc = 1: ")
for p in dssp:
    print(p)
id = 2
spc.connect()
sp = spc.Lay_ChiTiet(id)
if sp != None:
    print("*"*20)
    print(sp)
id_remove = 10
spc.connect()
result = spc.Xoa_SanPham(id_remove)
if result > 0:
    print("Xoa sp co ma =", id_remove,"thanh cong")
else:
    print("Xoa sp co ma =", id_remove,"that bai")