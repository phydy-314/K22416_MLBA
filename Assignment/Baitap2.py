from flask import Flask
from flaskext.mysql import MySQL
import pandas as pd
import seaborn as sns
import plotly.express as px
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score
import numpy as np
import matplotlib.pyplot as plt

app = Flask(__name__)


def getConnect(server, port, database, username, password):
    try:
        mysql = MySQL()
        app.config['MYSQL_DATABASE_HOST'] = server
        app.config['MYSQL_DATABASE_PORT'] = port
        app.config['MYSQL_DATABASE_DB'] = database
        app.config['MYSQL_DATABASE_USER'] = username
        app.config['MYSQL_DATABASE_PASSWORD'] = password
        mysql.init_app(app)
        conn = mysql.connect()
        return conn
    except mysql.connector.Error as e:
        print("Error =", e)
    return None


def closeConnection(conn):
    if conn is not None:
        conn.close()


def queryDataset(conn, sql):
    cursor = conn.cursor()
    cursor.execute(sql)
    df = pd.DataFrame(cursor.fetchall())
    return df


# Kết nối đến database sakila
conn = getConnect('localhost', 8000, 'sakila', 'root', 'Phydy@1311')

# Truy vấn dữ liệu: Tổng chi tiêu, tần suất thuê, và thể loại yêu thích
sql = """
SELECT 
    c.customer_id,
    c.first_name,
    c.last_name,
    SUM(p.amount) AS total_payment,
    COUNT(r.rental_id) AS rental_frequency,
    (
        SELECT fcat.category_id
        FROM rental r2
        JOIN inventory i ON r2.inventory_id = i.inventory_id
        JOIN film f ON i.film_id = f.film_id
        JOIN film_category fcat ON f.film_id = fcat.film_id
        WHERE r2.customer_id = c.customer_id
        GROUP BY fcat.category_id
        ORDER BY COUNT(*) DESC
        LIMIT 1
    ) AS favorite_genre
FROM customer c
LEFT JOIN rental r ON c.customer_id = r.customer_id
LEFT JOIN payment p ON c.customer_id = p.customer_id
GROUP BY c.customer_id, c.first_name, c.last_name
HAVING favorite_genre IS NOT NULL
"""
df = queryDataset(conn, sql)

# Đặt tên cột cho DataFrame
df.columns = ['CustomerId', 'FirstName', 'LastName', 'TotalPayment', 'RentalFrequency', 'FavoriteGenre']

# Loại bỏ các hàng có giá trị NaN
df = df.dropna()

# In dữ liệu
print(df.head())
print(df.describe())

# Chuẩn hóa dữ liệu
scaler = StandardScaler()
columns_to_cluster = ['TotalPayment', 'RentalFrequency', 'FavoriteGenre']
X = scaler.fit_transform(df[columns_to_cluster])


# Phương pháp Elbow và Silhouette để xác định số cụm tối ưu
def find_optimal_clusters(X, max_k=10):
    inertia = []
    silhouette_scores = []
    for k in range(2, max_k + 1):
        kmeans = KMeans(n_clusters=k, init='k-means++', max_iter=500, random_state=42)
        kmeans.fit(X)
        inertia.append(kmeans.inertia_)
        if k > 1:
            score = silhouette_score(X, kmeans.labels_)
            silhouette_scores.append(score)

    # Vẽ biểu đồ Elbow
    plt.figure(figsize=(15, 6))
    plt.subplot(1, 2, 1)
    plt.plot(range(2, max_k + 1), inertia, 'o-')
    plt.xlabel('Number of Clusters')
    plt.ylabel('Inertia')
    plt.title('Elbow Method')

    # Vẽ biểu đồ Silhouette
    plt.subplot(1, 2, 2)
    plt.plot(range(2, max_k + 1), silhouette_scores, 'o-')
    plt.xlabel('Number of Clusters')
    plt.ylabel('Silhouette Score')
    plt.title('Silhouette Score')
    plt.show()


# Tìm số cụm tối ưu
find_optimal_clusters(X)

# Chọn số cụm (giả sử Silhouette Score cho thấy k=5 là tối ưu)
cluster = 5
kmeans = KMeans(n_clusters=cluster, init='k-means++', max_iter=500, random_state=42)
y_kmeans = kmeans.fit_predict(X)
centroids = scaler.inverse_transform(kmeans.cluster_centers_)  # Chuyển centroids về giá trị gốc
df['cluster'] = y_kmeans


# --- Biểu đồ 1: Pair Plot ---
def plot_pair_plot(df, columns, hue):
    sns.pairplot(df, vars=columns, hue=hue, palette='Set1')
    plt.suptitle('Pair Plot of Features by Cluster', y=1.02)
    plt.show()


plot_pair_plot(df, columns_to_cluster, 'cluster')


# --- Biểu đồ 2: Box Plot ---
def plot_box_plots(df, columns, hue):
    plt.figure(figsize=(15, 5))
    for i, col in enumerate(columns, 1):
        plt.subplot(1, len(columns), i)
        sns.boxplot(x='cluster', y=col, data=df, hue='cluster', palette='Set1', legend=False)
        plt.title(f'Box Plot of {col} by Cluster')
    plt.tight_layout()
    plt.show()


plot_box_plots(df, columns_to_cluster, 'cluster')


# --- Biểu đồ 3: Scatter Plot với Centroids ---
def plot_scatter_with_centroids(df, x_col, y_col, hue, centroids, colors):
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=df, x=x_col, y=y_col, hue=hue, palette=colors, s=100, alpha=0.6)
    plt.scatter(centroids[:, 0], centroids[:, 1], s=300, c='black', marker='X', label='Centroids')
    plt.title(f'Scatter Plot of {x_col} vs {y_col} by Cluster')
    plt.xlabel(x_col)
    plt.ylabel(y_col)
    plt.legend()
    plt.show()


# Chọn hai đặc trưng để vẽ scatter plot
colors = sns.color_palette('Set1', n_colors=cluster)
plot_scatter_with_centroids(df, 'TotalPayment', 'RentalFrequency', 'cluster', centroids[:, [0, 1]], colors)


# --- Biểu đồ 4: 3D Scatter Plot ---
def visualize3DKmeans(df, columns, hover_data, cluster):
    fig = px.scatter_3d(
        df,
        x=columns[0],
        y=columns[1],
        z=columns[2],
        color='cluster',
        hover_data=hover_data,
        category_orders={"cluster": range(0, cluster)},
        labels={
            columns[0]: "Total Payment",
            columns[1]: "Rental Frequency",
            columns[2]: "Favorite Genre"
        },
        title="3D Scatter Plot of Customer Clusters"
    )
    fig.update_layout(margin=dict(l=0, r=0, b=0, t=30))
    fig.show()


# Dữ liệu để hiển thị khi hover
hover_data = ['CustomerId', 'FirstName', 'LastName']
visualize3DKmeans(df, columns_to_cluster, hover_data, cluster)


# Hàm lấy dữ liệu theo cụm
def get_customer_by_clusters(df, k):
    if k not in df["cluster"].unique():
        print(f"Cluster {k} không tồn tại trong dữ liệu.")
        return None
    cluster_data = df[df["cluster"] == k]
    print(f"\nCluster {k}: {len(cluster_data)} Customers\n")
    print(cluster_data[['CustomerId', 'TotalPayment', 'RentalFrequency', 'FavoriteGenre', 'cluster']].head(10))
    print("-" * 50)
    return cluster_data


# Xem dữ liệu của một cụm cụ thể
get_customer_by_clusters(df, 2)

# Đóng kết nối
closeConnection(conn)