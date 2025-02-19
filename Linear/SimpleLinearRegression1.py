import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt
import numpy as np
# Dữ liệu x và y
x = np.array([[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]).T
y = np.array([[2, 4, 3, 6, 9, 12, 13, 15, 18, 20]]).T


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
    plt.figure(figsize=(14, 8))
    plt.plot(x, y, 'r-o', label="value sample")  # Vẽ dữ liệu gốc

    # Tìm min/max của x và y
    x_min = np.min(x)
    x_max = np.max(x)
    y_min = np.min(y)
    y_max = np.max(y)

    # Đường trung bình y
    ybar = np.mean(y)

    # Vẽ đường ngang y = mean
    plt.axhline(ybar, linestyle='--', linewidth=4, label="mean")
    plt.axis([x_min * 0.95, x_max * 1.05, y_min * 0.95, y_max * 1.05])

    # Nhãn trục và tiêu đề
    plt.xlabel(xlabel, fontsize=16)
    plt.ylabel(ylabel, fontsize=16)
    plt.text(x_min, ybar * 1.01, "mean", fontsize=16)  # Hiển thị chữ "mean" trên đồ thị
    plt.legend(fontsize=15)
    plt.title(title, fontsize=20)
    plt.show()

# Gọi hàm hiển thị
showGraph(
    x=np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),
    y=np.array([2, 4, 3, 6, 9, 12, 13, 15, 18, 20]),
    title="Giá trị Y theo X",
    xlabel="Giá trị X",
    ylabel="Giá trị Y"
)
