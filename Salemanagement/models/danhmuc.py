class DanhMuc:
    def __init__(self, id, madanhmuc, tendanhmuc):
        self.id = id
        self.madanhmuc = madanhmuc
        self.tendanhmuc = tendanhmuc

    def __str__(self):
        return f"ID: {self.id}\nMã danh mục: {self.madanhmuc}\nTên danh mục: {self.tendanhmuc}"
