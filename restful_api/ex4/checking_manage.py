from flask import jsonify, request
from db import cursor, cnxn
from customer_manage import incr_acc_quantity, check_acc_no_exist, check_customer_id_exist
from restful_api.ex4.validator import validate_ca_add


def show_checking_acc():
    cursor.execute("Select * from checking_account")
    data = cursor.fetchall()
    ca_li = []
    for item in data:
        ca = {'id': item[0], 'customer_id': item[1], 'acc_no': item[2],
              'balance': item[3], 'link_code': item[4]}
        ca_li.append(ca)
    if ca_li:
        return jsonify({'checking account': ca_li})
    else:
        return jsonify({'mess':'no checking account is found'})


def add_checking_acc():
    data = request.get_json()
    customer_id = data['customer_id']
    acc_no = data['acc_no']
    balance = data['balance']
    link_code = data['link_code']
    validate = validate_ca_add(data)
    if validate != True:
        return jsonify({'mess': validate})
    else:
        if not check_customer_id_exist(customer_id):
            return jsonify({'mess': 'customer is not exist'})
        else:
            if check_acc_no_exist(acc_no):
                return jsonify({'mess': 'acc_no is exist'})
            else:
                cursor.execute('insert saving_account values (?,?,?,?)', customer_id, acc_no, balance, link_code)
                cnxn.commit()
                incr_acc_quantity(customer_id)
                return show_checking_acc()


def get_checking_acc_by_cid(id):
    cursor.execute("Select * from checking_account where customer_id = ?", id)
    data2 = cursor.fetchall()
    ca_li = []
    for item in data2:
        ca = {'id': item[0], 'customer_id': item[1], 'acc_no': item[2],
              'balance': item[3], 'link_code': item[4]}
        ca_li.append(ca)
    return ca_li


def show_checking_acc_by_cid(id):
    ca = get_checking_acc_by_cid(id)
    if ca:
        return jsonify({'checking acc': ca})
    else:
        return jsonify({'mess': 'no checking account is found'})