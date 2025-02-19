from flask import Flask, request, render_template, session, redirect, app
import numpy as np
import pandas as pd

from listLibs.utils import find_and_sort_orders1
app=Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def main():
    if request.method == "POST":
        min_value = float(request.form["min_value"])
        max_value = float(request.form["max_value"])
        sort_type = request.form.get("sort_type", "asc") == "asc"  # Kiểm tra giá trị sắp xếp (asc/tăng dần)

        # Đọc dữ liệu và xử lý
        df = pd.read_csv('Dataset/SalesTransactions.csv')
        result = find_and_sort_orders1(df, min_value, max_value, sort_type)

        return render_template(
            "orderss_sort.html",
            tables=[result.to_html(classes='data')],
            titles=result.columns.values,
            min_value=min_value,
            max_value=max_value,
            sort_type="asc" if sort_type else "desc"
        )
    else:
        return render_template("orderss_sort.html")

if __name__ =="__main__":
    app.run(host="localhost",port=9000,debug=True)
