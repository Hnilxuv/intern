from flask import Flask, request, render_template, url_for

from werkzeug.utils import redirect

app = Flask(__name__)
import pyodbc
driver= '{ODBC Driver 17 for SQL Server}'

cnx = pyodbc.connect( Trusted_Connection='yes',
                      Driver='{ODBC Driver 17 for SQL Server}',
                      Server='HNILXUV\SQLEXPRESS',
                      Database='sale_manage')
cursor = cnx.cursor()

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/Product')
def product_show():
    cursor.execute("SELECT * FROM PRODUCT")
    data = cursor.fetchall()
    ata = cursor.fetchall()
    pr_list = []
    for row in data:
        pr_list.append(row)
    return render_template("Product.html", pr_list=pr_list)

@app.route('/Product/add', methods=["POST"])
def product_add():
    name = request.form.get('name')
    category = request.form.get('category')
    brand = request.form.get('brand')
    price = request.form.get('price')
    if (name != "" or category != "" or brand != "" or price != ""):
        cursor.execute("insert PRODUCT values (?,?,?,?)", name, category, brand, int(price))
        cnx.commit()
        return redirect(url_for('index'))
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True, port=8080, use_reloader=False)
