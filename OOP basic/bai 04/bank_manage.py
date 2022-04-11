#lop khach hang
class customer:
    def __init__(self, id, name ):
        self.id = id
        self.name = name

#lop tai khoan
class account_bank(customer):
    def __init__(self, id, name, account_number, balance):
        super().__init__(id,name)
        self.account_number = account_number
        self.balance = balance

#lop tai khoan tiet kiem
class saving_account(account_bank):
    def __init__(self, id, name, account_number, balance, bank_interest_rate, link_code):
        super().__init__(id, name, account_number, balance)
        self.bir = bank_interest_rate
        self.link_code = link_code

    def get_account_number(self):
        return self.account_number

#lop tai khoan vang lai
class checking_account(account_bank):
    def __init__(self,id, name, account_number, balance,  link_code):
        super().__init__(id, name, account_number, balance)
        self.link_code = link_code

    def get_account_number(self):
        return self.account_number

#quan ly khach hang
class customer_manage:
    #khoi tao danh sach khach hang
    list_customer = []
    #khoi tao ma khach hang
    def generate_id(self):
        maxId = 1
        if self.customer_quantity() > 0:
            maxId = self.list_customer[0].id
            for pr in self.list_customer:
                if maxId < pr.id:
                    maxId = pr.id
            maxId = maxId + 1
        return maxId

    def customer_quantity(self):
        return len(self.list_customer)

    def add_customer(self):
        #khoi tao khach hang moi
        id = self.generate_id()
        name = input("Enter customer name: ")
        c = customer(id, name)
        self.list_customer.append(c)


    def show_customer_list(self, list_c):
        #hien thi danh sach khach hang
        print("{:<10} {:<25}  ".format("ID", "Customer Name" ))
        for i in list_c:
            print("{:<10} {:<25} ".format(i.id, i.name))
        print("\n")

    def get_customer_list(self):
        return self.list_customer

    #tim khach hang theo ma
    def find_by_id(self, id):
        rs = None
        for sa in self.list_customer:
            if sa.id == id:
                rs = sa
        return rs

class manage_saving_accounts:
    #khoi tao danh sach tai khoan tiet kiem
    list_saving_account = []


    def add_saving_account(self, id):
        #tao tai khoan tiet kiem
        customer_id = id
        name_customer = customer_manage().find_by_id(id).name
        account_number = input("Enter account number: ")
        balance = int(input("Enter balance : "))
        bank_ir = balance*10/100
        link_code = input("Enter account link code: ")
        sa = saving_account(customer_id, name_customer, account_number, balance, bank_ir, link_code)
        self.list_saving_account.append(sa)

    #tim tai khoan tiet kiem theo id khach hang
    def find_by_id(self, id):
        list_sa = []
        for sa in self.list_saving_account:
            if (sa.id == id):
                list_sa.append(sa)
        return list_sa
    #hien thi danh sach tai khoan tiet kiem
    def show_saving_account(self, list_sa):
        print("{:<15} {:<20} {:<15} {:<15} {:<15} {:<15}".format("Customer Id", "Name", "Account Number", "Balance", "Bank IR", "Link Code"))
        for i in list_sa:
            print("{:<15} {:<20} {:<15} {:<15} {:<15} {:<15}".format(i.id, i.name, i.account_number, i.balance, i.bir, i.link_code))
        print("\n")

    def get_list_sa(self):
        return self.list_saving_account

class manage_checking_accounts:
    list_checking_account = []

    def add_checking_account(self, id):
        customer_id = id
        name_customer = customer_manage().find_by_id(id).name
        account_number = input("Enter account number: ")
        balance = int(input("Enter balance : "))
        link_code = input("Enter account link code: ")
        ca = checking_account(customer_id, name_customer, account_number, balance, link_code)
        self.list_checking_account.append(ca)


    def find_by_id(self, id):
        list_ca = []
        for ca in self.list_checking_account:
            if (ca.id == id):
                list_ca.append(ca)
        return list_ca

    def show_saving_account(self, list_ca):
        print("{:<15} {:<20} {:<15} {:<15} {:<15}".format("Customer Id","Name", "Account Number", "Balance", "Link Code"))
        for i in list_ca:
            print("{:<20} {:<15} {:<15} {:<15} ".format(i.id, i.name, i.account_number, i.balance, i.link_code))
        print("\n")

    def get_list_ca(self):
        return self.list_checking_account