import random as r
from datetime import datetime


# lop san pham
class Product:
    def __init__(self, product_id, product_name, category, brand, price):
        self.id = product_id
        self.product_name = product_name
        self.category = category
        self.brand = brand
        self.price = price


# lop khach hang
class Customer:
    def __init__(self, customer_id, customer_name, phone):
        self.id = customer_id
        self.name = customer_name
        self.phone = phone


# cac ham quan li san pham
class ProductManage:
    list_product = []

    def generate_id(self):
        max_id = 1
        if self.product_amount() > 0:
            max_id = self.list_product[0].id
            for pr in self.list_product:
                if max_id < pr.id:
                    max_id = pr.id
            max_id = max_id + 1
        return max_id

    def product_amount(self):
        return len(self.list_product)

    def input_product(self):
        product_id = self.generate_id()
        name = input("Enter product name: ")
        category = input("Enter product category: ")
        brand = input("Enter product brand: ")
        price = int(input("Enter product price: "))
        while price < 0:
            price = int(input("Enter product price: "))
        prd = Product(product_id, name, category, brand, price)
        self.list_product.append(prd)
        f = open('products.txt', 'a')
        for item in self.list_product:
            f.write("{:<8} {:<18} {:<15} {:<15} {:<15}".format(item.id, item.product_name, item.category, item.brand,
                                                               item.price))
            f.write("%s\n" % "")
        f.close()

    def show_product_list(self, list_product):
        print("{:<15} {:<18} {:<10} {:<10} {:<10}".format("Product ID", "Name", "Catogory", "Brand", "Price"))
        for i in list_product:
            print("{:<20} {:<18} {:<10} {:<10} {:<10}".format(i.id, i.product_name, i.category, i.brand, i.price))
        print("\n")

    def get_product_list(self):
        return self.list_product


# ham sinh tu dong ma khach hang theo chuan UUID
def generate_uuid():
    random_string = ''
    random_str_seq = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    uuid_format = [3, 4]
    for n in uuid_format:
        for i in range(0, n):
            random_string += str(random_str_seq[r.randint(0, len(random_str_seq) - 1)])
        if n != 4:
            random_string += '-'
    return random_string


# cac ham quan ly khach hang
class CustomerManage:
    list_customer = []

    def input_customer(self):
        customer_id = generate_uuid()
        name = input("Enter customer name: ")
        phone = input("Enter customer phone: ")
        cus = Customer(customer_id, name, phone)
        self.list_customer.append(cus)
        f = open('customer.txt', 'a')
        for item in self.list_customer:
            f.write("{:<10} {:<18} {:<8} ".format(item.id, item.name, item.phone))
            f.write("%s\n" % "")
        f.close()

    def customer_amount(self):
        return len(self.list_customer)

    def show_customer_list(self, list_customer):
        print("{:<20} {:<18} {:<10} ".format("Customer ID", "Name", "Phone"))
        for i in list_customer:
            print("{:<20} {:<18} {:<10}".format(i.id, i.name, i.phone))
        print("\n")

    def get_customer_list(self):
        return self.list_customer

    def find_by_id(self, ID):
        list = []
        if self.customer_amount() > 0:
            for i in self.list_customer:
                if i.id == ID:
                    list.append(i)
        return list


# lop doi tuong hoa don
class Bill:

    def __init__(self, bill_id, time, customer_id, customer_name):
        self.id = bill_id
        self.time = time
        self.customer_id = customer_id
        self.customer_name = customer_name


# lop doi tuong chi tiet hoa don
class BillDetails:

    def __init__(self, bill_id, product_id, quantity):
        self.bill_id = bill_id
        self.product_id = product_id
        self.quantity = quantity


class BillManage:
    list_bill = []

    def generate_id(self):
        max_id = 1
        if self.bill_amount() > 0:
            max_id = self.list_bill[0].id
            for pr in self.list_bill:
                if max_id < pr.id:
                    max_id = pr.id
            max_id = max_id + 1
        return max_id

    def bill_amount(self):
        return len(self.list_bill)

    def input_bill(self):
        bill_id = self.generate_id()
        time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        customer_id = input("Enter customer id: ")
        customer_name = input("Enter customer name: ")
        b = Bill(bill_id, time, customer_id, customer_name)
        self.list_bill.append(b)

    def show_bill_list(self, list_bill):
        print("{:<8} {:<20} {:<15} {:<8}"
              .format("ID", "Time", "Customer ID", "Customer Name", ))
        if len(list_bill) > 0:
            for i in list_bill:
                print("{:<8} {:<20} {:<15} {:<8}".format(i.id, i.time, i.customer_id, i.customer_name))
        print("\n")

    def find_by_billid(self, id):
        rs = None
        if self.bill_amount() > 0:
            for b in self.list_bill:
                if b.id == id:
                    rs = b
        return rs

    def find_by_customer_id(self, id):
        list = []
        if self.bill_amount() > 0:
            for i in self.list_bill:
                if i.customer_id == id:
                    list.append(i)
        return list

    def get_bill_list(self):
        return self.list_bill


class BillDetailManage:
    list_bill_details = []

    def input_bill_details(self, id):
        bill_id = id
        customer_id = input("Enter ProductID: ")
        quantity = int(input("Enter Product Quantity: "))
        billdt = BillDetails(bill_id, customer_id, quantity)
        self.list_bill_details.append(billdt)

    def bill_detail_amount(self):
        return len(self.list_bill_details)

    def show_bill_details_list(self, list_bill_details):
        print("{:<8} {:<20} {:<15} ".format("Bill ID", "Produce ID", "Quantity"))
        for i in list_bill_details:
            print("{:<8} {:<20} {:<15}".format(i.bill_id, i.product_id, i.quantity))
        print("\n")

    def find_by_id(self, ID):
        list = []
        if self.bill_detail_amount() > 0:
            for i in self.list_bill_details:
                if i.bill_id == ID:
                    list.append(i)
        return list

    def get_list_bill_detail(self):
        return self.list_bill_details

