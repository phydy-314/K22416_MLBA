dataset =[]
dataset.append({"id":1,"name":"thuốc trị ghẻ","price":80})
dataset.append({"id":2,"name":"thuốc trị hôi nách","price":100})
dataset.append({"id":3,"name":"thuốc tăng tự tin","price":70})

def print_data():
    for product in dataset: 
        id = product["id"]
        name = product['name']
        price = product['price']
        infor = f"{id}\t{name}\t{price}"
        print(infor)

# sắp xếp giá trị =
def sort_data():
    for i in range(0,len(dataset)):
        for j in range(i+1, len(dataset)):
            pi = dataset[i]
            pj = dataset[j]
            if pi["price"] > pj["price"]:
                dataset[i] = pj
                dataset[j] = pi
sort_data()
print("Danh sách sản phẩm sau khi sắp xếp giá tăng dần:")
print_data()

# def add_product():
#     id = int(input("Nhập mã :"))
#     name = input("Nhập tên:")
#     price = float(input("Nhập giá:"))
#     product = {"id":id,"name":name,"price":price}
#     dataset.append(product)
print("Mời bạn nhập vào sản phẩm mới")
add_product()
print("Danh sách sản phẩm sau khi nhập mới:")
print_data()

dataset[0] = {"id":113,"name":"Thuốc cảm cúm","price":20}
print("Danh sách sản phẩm sau khi cập nhật:")
print_data()

dataset.pop(1)
print("Danh sách sản phẩm sau khi xóa:")
print_data()
