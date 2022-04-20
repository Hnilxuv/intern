from flask import jsonify, request
from db import cursor, cnxn
from validator import validate_cus_add


def show_customer():
    cursor.execute("Select * from customer")
    data = cursor.fetchall()
    cus_list = []
    for item in data:
        cus = {'id': item[0], 'name': item[1], 'acc_quantity': item[2]}
        cus_list.append(cus)
    return jsonify({'customer': cus_list})


def add_customer():
    data = request.get_json()
    name = data['name']
    acc_quantity = 0
    validate = validate_cus_add(data)
    if validate != True:
        return jsonify({'mess': validate_cus_add(data)})
    else:
        cursor.execute("Insert customer values (?,?)", name, acc_quantity)
        cnxn.commit()
        return show_customer()


def get_customer_by_id(id):
    cursor.execute("Select * from customer where customer_id = ?", id)
    data = cursor.fetchall()
    cus_list = []
    for item in data:
        cus = {'id': item[0], 'name': item[1], 'acc_quantity': item[2]}
        cus_list.append(cus)
    return cus_list


def show_cus_by_id(id):
    cus = get_customer_by_id(id)
    return jsonify({'customer': cus})


def incr_acc_quantity(customer_id):
    cursor.execute("select acc_quantity from customer where customer_id = ?", customer_id)
    acc_quantity = cursor.fetchone()
    tmp = acc_quantity[0] + 1
    cursor.execute("update customer set acc_quantity = ? where customer_id = ?", tmp, customer_id)
    cnxn.commit()


def check_acc_no_exist(acc_no):
    cursor.execute("select acc_no from saving_account checking_account where acc_no =?", acc_no)
    data = cursor.fetchall()
    if len(data) == 1:
        return True
    else:
        return False


def check_customer_id_exist(id):
    cursor.execute("select customer_id from customer where customer_id =?", id)
    data = cursor.fetchall()
    if len(data) == 1:
        return True
    else:
        return False


