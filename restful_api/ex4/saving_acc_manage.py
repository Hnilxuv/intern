from flask import jsonify, request
from db import cursor, cnxn
from validator import validate_sa_add
from customer_manage import incr_acc_quantity, check_acc_no_exist, check_customer_id_exist


def show_saving_acc():
    cursor.execute("Select * from saving_account")
    data = cursor.fetchall()
    sa_li = []
    for item in data:
        sa = {'id': item[0], 'customer_id': item[1], 'acc_no': item[2],
              'balance': item[3], 'interest_rate': item[4], 'link_code': item[5]}
        sa_li.append(sa)
    if sa_li:
        return jsonify({'saving account': sa_li})
    else:
        return jsonify({'no saving account is found'})


def add_saving_acc():
    data = request.get_json()
    customer_id = data['customer_id']
    acc_no = data['acc_no']
    balance = data['balance']
    ir = int(balance/100)
    link_code = data['link_code']
    validate = validate_sa_add(data)
    if validate != True:
        return jsonify({'mess': validate})
    else:
        if not check_customer_id_exist(customer_id):
            return jsonify({'mess': 'customer is not exist'})
        else:
            if check_acc_no_exist(acc_no):
                return jsonify({'mess': 'acc_no is exist'})
            else:
                cursor.execute('insert saving_account values (?,?,?,?,?)', customer_id, acc_no, balance, ir, link_code)
                cnxn.commit()
                incr_acc_quantity(customer_id)
                return show_saving_acc()


def get_saving_acc_by_cid(id):
    cursor.execute("Select * from saving_account where customer_id = ?", id)
    data1 = cursor.fetchall()
    sa_li = []
    for item in data1:
        sa = {'id': item[0], 'customer_id': item[1], 'acc_no': item[2],
              'balance': item[3], 'interest_rate': item[4], 'link_code': item[5]}
        sa_li.append(sa)
    return sa_li


def show_saving_acc_by_id(id):
    sa = get_saving_acc_by_cid(id)
    if sa:
        return jsonify({'saving acc': sa})
    else:
        return jsonify({'no saving account is found'})


def deposit_saving_acc(id):
    if get_saving_acc_by_cid(id):
        amount = request.json['amount']
        if amount > 0:
            a = cursor.execute("Select balance from saving_account where id= ?", id)
            balance = a.fetchone()
            tmp = balance[0] + amount
            cursor.execute("update saving_account set balance = ? where id= ?", (tmp, id))
            cnxn.commit()
            show_saving_acc_by_id(id)
        else:
            return 'invalid data'
    else:
        return jsonify({'no saving account is found'})