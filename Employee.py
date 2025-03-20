#EMPLOYEE.PY


import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="KsaU3*>6",
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
            Employee_Menu()

def add_category():
    cursor.execute("SELECT MAX(Category_ID) FROM category")
    result = cursor.fetchone()[0]
    if result is None:
        result = 0
    Category_ID = str(int(result) + 15)
    Category_Name = input("Enter Category Name: ")
    sql_query = "INSERT INTO category (Category_Name, Category_ID) VALUES (%s, %s)"
    #print(sql_query)
    try:
        cursor.execute(sql_query, (Category_Name, Category_ID))
        mydb.commit()
        print("Category added successfully!")
    except Exception as e:
        print("Error adding category:", e)
    Employee_Menu()


def add_product():
    cursor.execute("SELECT MAX(Product_ID) FROM Product")
    result = cursor.fetchone()
    Product_ID = f"{int(result[0])+2}"
    Category_ID = input("Enter Category ID: ")
    Product_Name = input("Enter Product Name: ")
    Product_Type = input("Enter Product Type: ")
    Price = float(input("Enter Product Price: "))
  
    cursor.execute("INSERT INTO product (Product_ID,Category_ID, Product_Name, Product_Type, Price) VALUES (%s, %s, %s, %s, %s)", (Product_ID,Category_ID, Product_Name, Product_Type, Price))
    print("Product Added Successfully!")
    Employee_Menu()


def update_product():
    Product_ID = input("Enter Product ID: ")
    cursor.execute("SELECT * FROM PRODUCT WHERE Product_ID = %s", (Product_ID,))
    product = cursor.fetchone()
    if product:
        print("1. Update Product Name")
        print("2. Update Product Type")
        print("3. Update Product Price")
        print("4. Back to Admin Menu")
        
     
        choice = input("Enter Your Choice: ")
        if choice == '1':
            Product_Name = input("Enter New Product Name: ")
            cursor.execute("UPDATE product SET Product_Name = %s WHERE Product_ID = %s", (Product_Name, Product_ID))
            mydb.commit()
            print("Product Name Updated Successfully!")
            update_product()
        elif choice == '2':
            Product_Type = input("Enter New Product Type: ")
            cursor.execute("UPDATE product SET Product_Type = %s WHERE Product_ID = %s", (Product_Type, Product_ID))
            mydb.commit()
            print("Product Type Updated Successfully!")
            update_product()
        elif choice == '3':
            Price = input("Enter New Product Price: ")
            cursor.execute("UPDATE product SET Price = %s WHERE Product_ID = %s", (Price, Product_ID))
            mydb.commit()
            print("Product Price Updated Successfully!")
            update_product()
       
 
        elif choice=="4":
            Employee_Menu()

def delete_customer():
    delme=(input("Enter Customer Name to be deleted: "))
    cursor.execute(f"DELETE FROM Cart WHERE Customer_Name={delme}")
    cursor.execute(f"DELETE FROM customer WHERE Customer_Name='{delme}'")
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