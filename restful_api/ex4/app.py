from flask import Flask, jsonify, request
import customer_manage as cm
import saving_acc_manage as sam
import checking_manage as cam

app = Flask(__name__)


@app.route('/customer')
def customer_show():
    return cm.show_customer()


@app.route('/customer/add')
def customer_add():
    return cm.add_customer()


@app.route('/saving_account')
def saving_account_show():
    return sam.show_saving_acc()


@app.route('/saving_account/add')
def saving_account_add():
    return sam.add_saving_acc()


@app.route('/checking_account')
def checking_account_show():
    return cam.show_checking_acc()


@app.route('/checking_account/add')
def checking_account_add():
    return cam.add_checking_acc()


@app.route('/customer/<int:id>')
def customer_detail(id):
    cus = cm.get_customer_by_id(id)
    sa_list = sam.get_saving_acc_by_cid(id)
    ca_list = cam.get_checking_acc_by_cid(id)
    return jsonify({'Customer': cus, 'saving acc': sa_list, 'checking acc': ca_list})


if __name__ == "__main__":
    app.run()
