class SanPham:
    def __init__(self, id, masanpham, tensanpham, soluong, dongia, iddanhmuc):
        self.id = id
        self.masanpham = masanpham
        self.tensanpham = tensanpham
        self.soluong = soluong
        self.dongia = dongia
        self.iddanhmuc = iddanhmuc

    def __str__(self):
        msg = f"ID: {self.id}\nMã sản phẩm: {self.masanpham}\nTên sản phẩm: {self.tensanpham}\nSố lượng: {self.soluong}\nĐơn giá: {self.dongia}\nID danh mục: {self.iddanhmuc}"
        return msg
