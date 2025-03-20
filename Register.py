#REGISTER.PY

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

def register():
    print("1. Register as Customer")
    print("2. Register as Employee")
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
    Customer_ID = result[0]+1

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
    Employee_ID = result[0] +"32"


    #Registering new Employee data in table
    query = f"INSERT INTO Employee (Employee_ID, Employee_Name, Gender,Contact_Number,Emergency_Contact_Number,Address,Email_ID,Passowrd,Medical_Specifics,Pay_Grade,Job_Title) VALUES ('{Employee_ID}', '{Employee_Name}', '{Gender}','{Contact_Number}', '{Emergency_Contact_Number}', '{Address}','{Email_ID}', '{Passowrd}', '{Medical_Specifics}','{Pay_Grade}','{Job_Title}')"
    cursor.execute(query)
    print("Employee registered")
    Employee_Menu()


#=================================================================================================================================================
