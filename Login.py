#LOGIN.PY


import mysql.connector
from Employee import *
from Customer import *


mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="KsaU3*>6",
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
    Password = input("Enter Employee Password: ")
    cursor.execute("SELECT * FROM Employee WHERE Email_ID = %s AND Passowrd = %s", (Email_ID,Password))
    employee = cursor.fetchone()
    if employee:
        print("Employee Logged in Successfully!")
        Employee_Menu()
    else:

        print("Invalid Login Credentials")
        print("====================================================================================================================")
        login()

Customer_ID=None
def Customer_Login():

    global Customer_ID
    Customer_ID=input("Enter Customer ID: ")
    Password_=input("Enter Password: ")
    cursor.execute("SELECT * FROM customer WHERE Customer_ID = %s AND Password_ = %s", (Customer_ID,Password_))
    customer = cursor.fetchone()
    if customer:
        print()
        print("Customer Logged in Successfully!")
        print("====================================================================================================================")
        Customer_Menu(Customer_ID)
    else:
        print("Invalid Login Credentials")
        login()

