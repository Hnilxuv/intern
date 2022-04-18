from bank_manage import manage_saving_accounts, manage_checking_accounts, customer_manage, customer

#khoi tao doi tuong quan ly
list_sa = manage_saving_accounts()
list_ca = manage_checking_accounts()
list_cus = customer_manage()

while True:
    print("\nBanking Management")
    print("*************************MENU**************************")
    print("**  1. Add Customer.                                 **")
    print("**  2. Show Customer List                            **")
    print("**  0. Exit.                                         **")
    key = int(input("Enter choose: "))

    if key == 1:
        print("\n1. Add Customer.")
        list_cus.add_customer()
        print("\nDone!")
    elif key == 2:
        print("\n2. Show Customer List.")
        list_cus.show_customer_list(list_cus.get_customer_list())
        id = int(input("Enter id: "))
        c: customer = list_cus.find_by_id(id)
        if c is not None:
            print("1. Add Saving Account.")
            print("2. Add Checking Account.")
            print("3. Show Account List.")
            print("0. Back")
            while True:
                key = int(input("Enter choose: "))
                if key == 1:
                    print("1. Add Saving Account.")
                    list_sa.add_saving_account(id)
                elif key == 2:
                    print("2. Add Checking Account.")
                    list_ca.add_checking_account(id)
                elif key == 3:
                    print("3. Show Account List.")
                    print("\n")
                    sa = len(list_sa.find_by_id(id))
                    ca = len(list_ca.find_by_id(id))
                    print("Total number of accounts", ca + sa)
                    print("1.Saving Account:", sa)
                    print("2.Checking Account:", ca)
                    print("0. Back")
                    while True:
                        key = int(input("Enter choose: "))
                        if key == 1:
                            print("1.Saving Account:")
                            list_sa.show_saving_account(list_sa.find_by_id(id))
                        elif key == 2:
                            print("2.Checking Account:")
                            list_ca.show_saving_account(list_ca.find_by_id(id))
                        elif key == 0:
                            print("\nBack")
                            break
                        else:
                            print("\nError choose!")
                            print("Again choose")

                elif key == 0:
                    print("\nBack")
                    break
                else:
                    print("\nError choose!")
                    print("\nAgain Choose")
        else:
            print("Customer does not exist")


