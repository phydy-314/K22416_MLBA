from Salemanagement.libs.danhmucconnector import DanhMucConnector

dmc = DanhMucConnector()
dmc.connect()
dsdm = dmc.LayToanBoDanhMuc()
print('Danh muc san pham cua he thong ')
for dm in dsdm:
    print(dm)