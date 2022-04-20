from flask import Flask
import customer_manage as cm
import bill_manage as bm
import product_manage as pm
import billdetail_manage as bdm


app = Flask(__name__)


@app.route('/Product')
def show_product():
    return pm.show_product()


@app.route('/Product/add')
def product_add():
    return pm.add_product()


@app.route('/Product/<int:id>')
def show_product_by_id(id):
    return pm.show_product_by_id(id)


@app.route('/Customer')
def show_customer():
    return cm.show_customer()


@app.route('/Customer/<string:id>')
def show_customer_by_id(id):
    return cm.show_customer_by_id(id)


@app.route('/Customer/add')
def customer_add():
    return cm.customer_add()


@app.route('/Customer/<string:id>/Bill')
def show_bill_by_customer_id(id):
    return bm.show_bill_by_cid(id)


@app.route('/Bill')
def show_bill():
    return bm.show_bill()


@app.route('/Bill/add')
def add_bill():
    return bm.add_bill()


@app.route('/Bill/<int:id>')
def show_bill_by_bill_id(id):
    return bm.show_bill_by_id(id)


@app.route('/Bill/<int:id>/detail')
def show_bill_detail_by_id(id):
    return bdm.show_bill_detail_by_id(id)


@app.route('/Bill/<int:id>/add')
def add_bill_detail(id):
    return bdm.bill_detail_add(id)


if __name__ == "__main__":
    app.run(debug=True, port=8080, use_reloader=False)
