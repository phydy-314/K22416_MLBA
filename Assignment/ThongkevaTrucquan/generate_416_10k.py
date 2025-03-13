import pandas as pd
import plotly.express as px
import numpy as np

# Bước 1: Tạo dữ liệu từ bảng
excel_file = "dataset-416.xlsx"
df = pd.read_excel(excel_file)
df = df[['Mã HP', 'Tên học phần', 'Loại môn học', 'Ngôn ngữ', 'Học Kỳ']].dropna()
df['Số tín chỉ'] = np.random.randint(1, 4, size=len(df))
# Tạo cột mới để gộp thông tin học phần
df['Học phần'] = df['Mã HP'] + ' - ' + df['Tên học phần']

# Bước 2: Tạo biểu đồ Sunburst
fig = px.sunburst(
    df,
    path=['Học Kỳ', 'Học phần'],
    values='Số tín chỉ',
    title='Chương trình đào tạo Thương mại điện tử - Kỳ 1 và Kỳ 2',
    color='Số tín chỉ',
    color_continuous_scale='Viridis',
    width=800,
    height=800
)

# Tùy chỉnh giao diện biểu đồ
fig.update_layout(
    title_font_size=20,
    margin=dict(t=50, l=0, r=0, b=0),
    font=dict(size=12),
)

# Bước 3: Xuất biểu đồ ra file HTML
fig.write_html("416_10k.html")
print("Đã tạo file 416_10k.html thành công!")