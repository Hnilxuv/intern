from sale_manage import Bill, ProductManage, CustomerManage, BillManage, BillDetailManage

list_product = ProductManage()
list_customer = CustomerManage()
list_bill = BillManage()
list_bill_details = BillDetailManage()

while (True):
    print("\nSale Management")
    print("*************************MENU**************************")
    print("**  1. Add Product.                                  **")
    print("**  2. Add Customer.                                 **")
    print("**  3. Create Bill.                                  **")
    print("**  4. Show Bill List.                               **")
    print("**  5. Show Customer Lists                           **")
    print("**  0. Exit.                                         **")
    key = int(input("Enter choose: "))
    if (key == 1):
        print("\n1. Add Product.")
        f = open("products.txt", "w")
        f.write("{:<8} {:<18} {:<15} {:<15} {:<15}".format("id", "Product Name", "Category", "Brand", "Price"))
        f.write("%s\n" % "")
        f.close()
        list_product.input_product()
        print("\nDone!")
    elif (key == 2):
        print("\n2. Add Customer.")
        f1 = open("customer.txt", "w")
        f1.write("{:<10} {:<18} {:<8}".format("id", "Customer Name", "Phone"))
        f1.write("%s\n" % "")
        f1.close()
        list_customer.input_customer()
        print("\nDone!")
    elif (key == 3):
        print("\n3. Create Bill.")
        list_customer.show_customer_list(list_customer.get_customer_list())
        print("\nEnter Bill Information:")
        list_bill.input_bill()
        list_product.show_product_list(list_product.get_product_list())
        id = int(input("Enter bill id: "))
        c: Bill = list_bill.find_by_billid(id)
        if(c!=None):
            print("1.Add Bill Detail.   ")
            print("2.Back               ")
            while(True):
                key1 = int(input("Enter choose: "))
                if(key1 == 1):
                    print("\nEnter Bill Detail.")
                    list_bill_details.input_bill_details(id)
                elif(key1 == 2):
                    print("\nDone")
                    break
        else:
            print("Bill does not exist")
    elif (key == 4):
        list_bill.show_bill_list(list_bill.get_bill_list())

        bid = int(input("Enter bill id to show bill detail: "))
        rs = list_bill_details.find_by_id(bid)
        list_bill_details.show_bill_details_list(rs)


    elif(key == 5):
        list_customer.show_customer_list(list_customer.get_customer_list())
        customer_id = input("Enter customer id: ")
        rs1 = list_bill.find_by_customer_id(customer_id)
        list_bill.show_bill_list(rs1)
        bill_id = int(input("Enter Bill ID to show bill detail: "))
        rs2 = list_bill_details.find_by_id(bill_id)
        list_bill_details.show_bill_details_list(rs2)
    elif key == 0:
        print("\nExit")
        break
    else:
        print("\nError choose!")
        print("\nEnter choose.")

