import pandas as pd

def find_orders_within_range(df, min_value, max_value):
    """
    Find unique order IDs within a specified range of total order values.

    Parameters:
        df (DataFrame): The input DataFrame containing sales transaction data.
        min_value (float): The minimum value of the order total range.
        max_value (float): The maximum value of the order total range.

    Returns:
        list: A list of unique order IDs within the specified range.
    """
    # Calculate total value for each order
    order_totals = df.groupby('OrderID').apply(
        lambda x: (x['UnitPrice'] * x['Quantity'] * (1 - x['Discount'])).sum()
    )

    # Filter orders within the specified range
    orders_within_range = order_totals[(order_totals >= min_value) & (order_totals <= max_value)]

    # Get unique order IDs within the range
    unique_orders = df[df['OrderID'].isin(orders_within_range.index)]['OrderID'].drop_duplicates().tolist()

    return unique_orders

if __name__ == "__main__":
    # Load data
    df = pd.read_csv('../dataset/SalesTransactions.csv')

    # Get input for minimum and maximum values
    min_value = float(input("Nhập giá trị min: "))
    max_value = float(input("Nhập giá trị max: "))

    # Find and display the result
    result = find_orders_within_range(df, min_value, max_value)
    print(f"Danh sách các hóa đơn trong phạm vi giá trị từ {min_value} đến {max_value} là:", result)
