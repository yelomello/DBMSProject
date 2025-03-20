#MAIN MENU.PY

import mysql.connector
from Customer import *
from Employee import *
from Login import *
from Register import *



# Connect to the database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="KsaU3*>6",
    database="molkerei"
)

def MainMenu():
    while True:
        print("1. Login")
        print("2. Register")
        print("3. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            login()
        elif choice == "2":
            register()
        elif choice == "3":
            break
                          
        else:
            print()
            print("Invalid")
            print()
            print("====================================================================================================================")
            print()

           

if __name__ == '__main__':
    MainMenu()
'''
#=================================================================================================================================================


#LOGIN.PY


import mysql.connector
from Employee import *
from Customer import *

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="ommeh",
    database="molkerei"
)

cursor = mydb.cursor()
mydb.autocommit=True

def login():
    print("1. Login as Employee")
    print("2. Login as Customer")
    print("3. Back")
    choice = input("Enter your choice: ")
    if choice == "1":
        Employee_Login()
    elif choice == "2":
        Customer_Login()
    elif choice == "3":
        main()
    else:
        print("Invalid choice. Please enter a number between 1 and 3.")
        login()

def Employee_Login():
    Email_ID = input("Enter Employee Email ID: ")
    Passowrd = input("Enter Employee Password: ")
    cursor.execute("SELECT * FROM Employee WHERE Email_ID = %s AND Passowrd = %s", (Email_ID,Passowrd))
    vendor = cursor.fetchone()
    if vendor:
        print("Employee Logged in Successfully!")
        vendor_menu()
    else:

        print("Invalid Login Credentials")
        print("====================================================================================================================")
        login()

def Customer_Login():
    Email_ID=input("Enter Email ID: ")
    Password_=input("Enter Password: ")
    cursor.execute("SELECT * FROM customer WHERE Email_ID = %s AND Password_ = %s", (Email_ID,Password_))
    user = cursor.fetchone()
    if user:
        print("User Logged in Successfully!")
        user_menu(user[0])
    else:
        print("Invalid Login Credentials")
        login()

#=================================================================================================================================================

#REGISTER.PY



cursor = mydb.cursor()
mydb.autocommit=True

def register():
    print("1. Register as Customer")
    print("2. Reister as Employee")
    print("3. Back")
    choice = input("Enter your choice: ")
    if choice == "1":
        register_customer()
    elif choice == "2":
        register_Employee()
   
    elif choice == "3":
        print("------------------------------------------------------------------------------------------------------")
        print()
        print()
    else:
        print("Invalid choice. Please enter a number between 1 and 3.")
        register()

def register_customer():
    print("Please enter the following details:")
    Customer_Name = input("Customer Name: ")
    Gender = input("Gender: ")
    Contact_Number = input("Customer Contact Number: ")
    Address = input("Customer Address: ")
    Email_ID = input("Customer Email ID: ")
    Password_ = input("Customer Password_: ")
    
    cursor.execute("SELECT MAX(Customer_ID) FROM customer")
    result = cursor.fetchone()
    Customer_ID = result[0]+27

    # Registering new customer data in table
    query = f"INSERT INTO customer (Customer_ID, Customer_Name, Password_, Gender, Contact_Number, Address, Email_ID) VALUES ('{Customer_ID}','{Customer_Name}','{Password_}','{Gender}','{Contact_Number}','{Address}','{Email_ID}')"
    cursor.execute(query)
    mydb.commit()
    print("User registered successfully!")
      

def register_Employee():
    print("Please enter the following details:")
    Employee_Name = input("Employee Name: ")
    Gender = input("Gender: ")
    Contact_Number = input("Customer Contact Number: ")
    Emergency_Contact_Number = input("Enter Emergency Contact Number: ")
    Address = input("Employee Address: ")
    Email_ID = input("Employee Email_ID: ")
    Passowrd = input("Enter Password: ")
    Medical_Specifics=input("Enter Medical Specifics: ")
    Pay_Grade=input("Enter Pay Grade: ")
    Job_Title=input("Enter Job Title: ")

    cursor.execute("SELECT MAX(Employee_ID) FROM employee")
    result = cursor.fetchone()
    Employee_ID = result[0] + 32


    #Registering new Employee data in table
    query = f"INSERT INTO Employee (Employee_ID, Employee_Name, Gender,Contact_Number,Emergency_Contact_Number,Address,Email_ID,Passowrd,Medical_Specifics,Pay_Grade,Job_Title) VALUES ('{Employee_ID}', '{Employee_Name}', '{Gender}','{Contact_Number}', '{Emergency_Contact_Number}', '{Address}','{Email_ID}', '{Passowrd}', '{Medical_Specifics}','{Pay_Grade}','{Job_Title}')"
    cursor.execute(query)
    print("Employee registered")
    admin_menu()


#=================================================================================================================================================


#CUSTOMER.PY

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="ommeh",
    database="molkerei"
)

cursor = mydb.cursor()
mydb.autocommit=True

def Customer_Menu(customer_id):
    print("Welcome to the user menu!\n")
    while True:
        print("Please choose an option:")
        print("1. View products")
        print("2. View cart")
        print("3. Add item to cart")
        print("4. Remove item from cart")
        print("5. Place order")
        print("6. Apply coupon")
        print("7. Review product")
        print("8. Logout")
        choice = input("Enter your choice: ")
        if choice == "1":
            view_products()
        elif choice == "2":
            view_cart(customer_id)
        elif choice == "3":
            add_to_cart(customer_id)
        elif choice == "4":
            remove_from_cart(customer_id)
        elif choice == "5":
            place_order(customer_id)
        elif choice == "6":
            apply_coupon(customer_id)
        elif choice == "7":
            rate_product(customer_id)
        elif choice == "8":
            main()
            break
        else:
            print("Invalid choice. Please try a number between (1-8)\n")

def view_products():
    # Get a cursor
    cursor = mydb.cursor()

    # Execute the query to fetch all products
    query = "SELECT Product_ID, Category_ID, Product_Name, Product_Type, Price FROM product"
    cursor.execute(query)

    # Fetch all the rows returned by the query
    products = cursor.fetchall()

    # Print the details of all the products
    print("Product Details:")
    for product in products:
        print(f"Product ID: {product[0]}, Category ID: {product[1]}, Name: {product[2]}, Type: {product[3]}, Price: {product[4]}")

    Customer_Menu()



def add_to_cart(customer_id):
    # Execute SQL query to check if the customer already has the product in their cart
    product_id = int(input("Enter the Product ID: "))
    quantity = int(input("Enter the Quantity: "))

    cursor.execute(f"SELECT * FROM Product WHERE Product_ID = '{product_id}'")
    product = cursor.fetchone()

    # If the product is available, add it to the customer's cart
    if product:
        cursor.execute(f"SELECT * FROM CART WHERE Customer_id = '{customer_id}' AND Product_id = '{product_id}'")
        cart_item = cursor.fetchone()

        # If the customer already has the product in their cart, update the quantity
        if cart_item:
            new_quantity = cart_item[2] + quantity
            cursor.execute(f"UPDATE CART SET Product_quantity = '{new_quantity}' WHERE Customer_id = '{customer_id}' AND Product_id = '{product_id}'")
            print(f"{quantity} {product[2]}(s) added to cart")
        # Otherwise, add a new cart item
        else:
            cursor.execute(f"INSERT INTO CART (Customer_id, Product_id, Product_quantity) VALUES ('{customer_id}', '{product_id}', '{quantity}')")
            print(f"{quantity} {product[2]}(s) added to cart")
    else:
        print("Product not found")
    print()

    Customer_Menu()

    
def checkout(customer_id):
    cursor.execute(f"SELECT * FROM cart WHERE customer_id = {customer_id}")
    cart_items = cursor.fetchall()

    if not cart_items:
        print("Your cart is empty.")
    else:
        print("Checking Out")
        total = 0
        for item in cart_items:
            cursor.execute(f"SELECT * FROM product WHERE Product_ID = {item[1]}")
            prod = cursor.fetchone()
            print(f"{item[2]} {prod[2]} added to your order.")
            total += item[2] * prod[4]

        print(f"\nTotal Order Value: {total}")
        print("Taking you to the payment portal.....\n")
        print("Thanks for the purchase.....")

        for item in cart_items:
            cursor.execute(f"DELETE FROM cart WHERE customer_id = {customer_id} AND product_id = {item[1]}")

    Customer_Menu()
        

    

def view_cart(customer_id):
    # Get the cart items for the given customer ID
    cursor.execute(f"SELECT * FROM cart WHERE customer_id = {customer_id}")
    cart_items = cursor.fetchall()

    if not cart_items:
        print("Your cart is empty.")
        Customer_Menu()

    else:
        print("Here are the items in your cart:")
        print("Product Name | Quantity | Total Price")
        total_price = 0
        for item in cart_items:
            cursor.execute(f"SELECT * FROM product WHERE Product_id = {item[1]}")
            prod = cursor.fetchone()
            name = prod[2]
            price = prod[4]
            quantity = item[2]
            total_item_price = quantity * price
            total_price += total_item_price
            print(f"{name}     {quantity}     {total_item_price}")
        
        print(f"Total Price: {total_price}")

    # Ask user if they want to checkout or continue shopping
    while True:
        checkout_choice = input("Enter '1' to checkout or '2' to continue shopping: ")
        if checkout_choice.lower() == "1":
            checkout(customer_id)
            break
        elif checkout_choice.lower() == "2":
            Customer_Menu(customer_id)
            break
        else:
            print("Invalid choice. Please enter '1' to checkout or '2' to continue shopping.")


def add_to_cart(customer_id):
    product_id = input("Enter the product ID you want to add to cart: ")
    product_quantity = int(input("Enter the quantity you want to add to cart: "))

    # Check if the product exists
    if db.get_product(Product_ID):
        db.add_to_cart(Customer_ID, Product_ID, Category_ID, Product_Name, Product_Type, Price)
        print("Product added to cart successfully!")
    else:
        print("Product not found!")


def remove_from_cart(customer_id):
    product_id = input("Enter the product ID you want to remove from cart: ")
    db.remove_from_cart(Customer_id, Product_id)
    print("Product removed from cart successfully!")

def place_order(customer_id):
    checkout(customer_id)

def apply_coupon(customer_id):
    Coupon_ID = input("Enter the coupon code: ")
    db.apply_coupon(Coupon_ID, Discount_Percentage)



def rate_product(customer_id):
    customer_ID = input("Enter you Customer ID: ")
    Rating = int(input("Enter the rating (1-5): "))
    Review = input("Enter your review: ")
    db.rate_product(customer_ID, Rating, Review)
    print("Product rated successfully!")
    Customer_Menu(customer_id)

#=================================================================================================================================================

#EMPLOYEE.PY


import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="ommeh",
    database="molkerei"
)

cursor = mydb.cursor()
mydb.autocommit=True


def Employee_Menu():
    while True:
        print("1. Add Category")
        print("2. Add Product")
        print("3. Update product")
        print("4. Delete Customer")
        print("5. Delete Employee")
        print("6. Delete Product")
        print("7. Logout")

        choice = input("Enter Your Choice: ")
        if choice == '1':
            add_category()
        elif choice == '2':
            add_product()
        elif choice == '3':
            update_product()
        elif choice == '4':
            delete_customer()
        elif choice == '5':
            delete_employee()
        elif choice == "6":
            delete_product()
        elif choice == "7":
            print("Logging Out")
            break
        else:
            print("Invalid Choice, please choose a number between (1-7)")
            admin_menu()

def add_category():
    cursor.execute("SELECT MAX(Category_ID) FROM category")
    result = cursor.fetchone()
    Category_ID = result[0]+15
    Category_Name = input("Enter Category Name: ")
    cursor.execute("INSERT INTO category (Category_Name, Category_ID) VALUES (%s, %s)", (Category_Name, Category_ID))
    print("Category Added Successfully!")
    Employee_Menu()

def add_product():
    cursor.execute("SELECT MAX(Product_id) FROM Product")
    result = cursor.fetchone()
    product_id = result[0]+61
    Category_ID = input("Enter Category ID: ")
    Product_Name = input("Enter Product Name: ")
    Product_Type = input("Enter Product Type: ")
    Price = float(input("Enter Product Price: "))
  
    cursor.execute("INSERT INTO product (Product_ID,Category_ID, Product_Name, Product_Type, Price) VALUES (%s, %s, %s, %s, %s)", (Product_ID,Category_ID, Product_Name, Product_Type, Price))
    print("Product Added Successfully!")
    Employee_Menu()


def update_product():
    product_id = input("Enter Product ID: ")
    cursor.execute("SELECT * FROM PRODUCT WHERE Product_id = %s", (product_id,))
    product = cursor.fetchone()
    if product:
        print("1. Update Product Name")
        print("2. Update Product Type")
        print("3. Update Product Price")
        print("4. Back to Admin Menu")
     
        choice = input("Enter Your Choice: ")
        if choice == '1':
            product_name = input("Enter New Product Name: ")
            cursor.execute("UPDATE product SET Product_Name = %s WHERE Product_ID = %s", (Product_Name, Product_ID))
            mydb.commit()
            print("Product Name Updated Successfully!")
            update_product()
        elif choice == '2':
            product_type = input("Enter New Product Type: ")
            cursor.execute("UPDATE product SET Product_Type = %s WHERE Product_ID = %s", (Product_Type, Product_ID))
            mydb.commit()
            print("Product Type Updated Successfully!")
            update_product()
        elif choice == '3':
            product_price = input("Enter New Product Price: ")
            cursor.execute("UPDATE product SET Price = %s WHERE Product_ID = %s", (Price, Product_ID))
            mydb.commit()
            print("Product Price Updated Successfully!")
            update_product()
       
 
        elif choice=="4":
            Employee_Menu()

def delete_customer():
    delme=int(input("Enter Customer ID to be deleted: "))
    cursor.execute(f"DELETE FROM Cart WHERE Customer_ID={delme}")
    cursor.execute(f"DELETE FROM customer WHERE Customer_ID={delme}")
    print("Customer deleted successfully!")
    Employee_Menu()


def delete_employee():
    delme = int(input("Enter Employee ID to be deleted: "))
    cursor.execute(f"SELECT Pay_Grade FROM employee WHERE Employee_ID={delme}")
    result = cursor.fetchone()
    if result and result[0] in ['E4', 'E3', 'E2', 'E1', 'E0']:
        cursor.execute(f"DELETE FROM employee WHERE Employee_ID={delme}")
        print("Employee deleted successfully!")
    else:
        print("Employee pay_grade is not within the allowed range. Deletion is not allowed.")
        
    Employee_Menu()    




def delete_product():
    delme=int(input("Enter product ID to be deleted: "))
    cursor.execute(f"DELETE FROM Cart WHERE Product_ID={delme}")
    cursor.execute(f"DELETE FROM PRODUCT WHERE Product_ID={delme}")
    print("Product deleted successfully!")

    Employee_Menu()
    '''