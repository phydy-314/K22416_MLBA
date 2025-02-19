from ontap_oop.filefactory import FileFactory
from ontap_oop.product import Product

p1 = Product(1,"Coca",100)
print(p1)
dataset = []
dataset.append(p1)
dataset.append(Product(2,"Pepsi",20))
dataset.append(Product(3,"Sting",80))
dataset.append(Product(4,"Aqua",70))
dataset.append(Product(5,"Redbull",50))
print("Danh sách sản phẩm:")
for product in dataset:
    print(product)

while True:
    id=(int(input("Nhập mã:")))
    name=input("Nhập tên:")
    price=float(input("Nhập giá:"))
    p=Product(id,name,price)
    dataset.append(p)
    ask=input("nhập tiếp không?(c/k):")
    if ask=='k':
        break
print("Danh sách sản phẩm sau khi nhập:")
for product in dataset:
    print(product)

#gọi chức năng chụp ảnh đối tượng xuống ổ cứng
#chụp thành định dạng json
ff = FileFactory()
ff.writeData("Mydataset.json",dataset)