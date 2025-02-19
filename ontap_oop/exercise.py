from ontap_oop.product import Product
dataset = []
dataset.append(Product(2,"Pepsi",20))
dataset.append(Product(3,"Sting",80))
dataset.append(Product(4,"Aqua",70))
dataset.append(Product(5,"Redbull",50))
def filter_products_by_price_range(dataset, min_price, max_price):
    """
    Lọc ra các sản phẩm có giá trong khoảng (min_price, max_price).
    """
    return [product for product in dataset if min_price <= product.price <= max_price]

def remove_products_below_price(dataset, threshold):
    """
    Xóa tất cả các sản phẩm có giá nhỏ hơn threshold.
    """
    return [product for product in dataset if product.price >= threshold]
        
# Ví dụ sử dụng
min_price = float(input("Nhập giá nhỏ nhất:"))
max_price = float(input("Nhập giá lớn nhất:"))
filtered_products = filter_products_by_price_range(dataset, min_price, max_price)
print(f"Các sản phẩm có giá từ {min_price} đến {max_price}:")
for product in filtered_products:
    print(product)

threshold = float(input("Nhập giá sản phẩm X:"))
dataset = remove_products_below_price(dataset, threshold)
print(f"Danh sách sản phẩm sau khi xóa các sản phẩm có giá nhỏ hơn {threshold}(X):")
for product in dataset:
    print(product)