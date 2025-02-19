import matplotlib.pyplot as plt
import numpy as np


# Dữ liệu diện tích (area) và giá (price)
x = np.array([[73.5, 75, 76.5, 79, 81.5, 82.5, 84, 85, 86.5, 87.5, 89, 90, 91.5]]).T
y = np.array([[1.49, 1.50, 1.51, 1.54, 1.58, 1.59, 1.60, 1.62, 1.63, 1.64, 1.66, 1.67, 1.68]]).T


# Hàm tính b1 và b0
def calculateb1b0(x, y):
    # Tính trung bình
    xbar = np.mean(x)
    ybar = np.mean(y)
    x2bar = np.mean(x ** 2)
    xybar = np.mean(x * y)

    # Tính b1 và b0
    b1 = (xbar * ybar - xybar) / (xbar ** 2 - x2bar)
    b0 = ybar - b1 * xbar
    return b1, b0


# Tính b1 và b0
b1, b0 = calculateb1b0(x, y)
print("b1=", b1)
print("b0=", b0)

# Hàm hiển thị biểu đồ
def showGraph(x, y, title="", xlabel="", ylabel=""):
    plt.figure(figsize=(14, 8))  # Kích thước đồ thị
    plt.plot(x, y, 'r-o', label="price")  # Vẽ dữ liệu thực tế

    # Tìm min/max của x và y
    x_min = np.min(x)
    x_max = np.max(x)
    y_min = np.min(y)
    y_max = np.max(y)

    # Tính giá trị trung bình của y
    ybar = np.mean(y)

    # Vẽ đường ngang tại giá trị trung bình của y
    plt.axhline(ybar, linestyle='--', linewidth=4, label="mean")
    plt.axis([x_min * 0.95, x_max * 1.05, y_min * 0.95, y_max * 1.05])  # Giới hạn trục

    # Gán nhãn trục và tiêu đề
    plt.xlabel(xlabel, fontsize=16)
    plt.ylabel(ylabel, fontsize=16)
    plt.text(x_min, ybar * 1.01, "mean", fontsize=16)  # Ghi chú "mean" trên đường trung bình
    plt.legend(fontsize=15)  # Thêm chú thích
    plt.title(title, fontsize=20)  # Tiêu đề
    plt.show()

# Dữ liệu diện tích (x) và giá nhà (y)
x = np.array([[73.5, 75, 76.5, 79, 81.5, 82.5, 84, 85, 86.5, 87.5, 89, 90, 91.5]]).T
y = np.array([[1.49, 1.50, 1.51, 1.54, 1.58, 1.59, 1.60, 1.62, 1.63, 1.64, 1.66, 1.67, 1.68]]).T

# Gọi hàm hiển thị
showGraph(
    x, y,
    title='Giá nhà theo diện tích',
    xlabel='Diện tích (m2)',
    ylabel='Giá nhà (tỷ VND)'
)
