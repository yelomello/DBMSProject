#CUSTOMER.PY

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="KsaU3*>6",
    database="molkerei"
)

cursor = mydb.cursor()
mydb.autocommit=True

def Customer_Menu(Customer_ID):
    print("Welcome to the Customer menu!\n")
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
            view_products(Customer_ID)
        elif choice == "2":
            view_cart(Customer_ID)
        elif choice == "3":
            add_to_cart()
        elif choice == "4":
            remove_from_cart(Customer_ID)
        elif choice == "5":
            place_order(Customer_ID)
        elif choice == "6":
            apply_coupon(Customer_ID)
        elif choice == "7":
            rate_product(Customer_ID)
        elif choice == "8":
            MainMenu()
            break
        else:
            print("Invalid choice. Please try a number between (1-8)\n")

def view_products(Customer_ID):
    # Get a cursor
    cursor = mydb.cursor()

    # Execute the query to fetch all products
    query = "SELECT Product_ID, Category_ID, Product_Name, Product_Type, Price FROM Product"
    cursor.execute(query)

    # Fetch all the rows returned by the query
    products = cursor.fetchall()

    # Print the details of all the products
    print("Product Details:")
    for product in products:
        print(f"Product ID: {product[0]}, Category ID: {product[1]}, Name: {product[2]}, Type: {product[3]}, Price: {product[4]}")
    print("--------------------------------------------------------------------------------------------------------------------------------")
    Customer_Menu(Customer_ID)

    
def checkout(Customer_ID):
    #global Customer_ID

    cursor.execute(f"SELECT * FROM Cart WHERE Customer_ID = {Customer_ID}")
    cart_items = cursor.fetchall()

    if not cart_items:
        print("Your cart is empty.")
    else:
        print("Checking Out")
        total = 0.0
        for item in cart_items:
            cursor.execute(f"SELECT * FROM Product WHERE Product_ID = {item[1]}")
            prod = cursor.fetchone()
            print(f"{item[2]} {prod[2]} added to your order.")
            (total) += float(item[2]) * float(prod[4])
        

        print(f"\nTotal Order Value: {total}")
        print("Taking you to the payment portal.....\n")
        print("Thanks for the purchase.....")

        for item in cart_items:
            cursor.execute(f"DELETE FROM cart WHERE customer_id = {Customer_ID} AND Product_ID = {item[1]}")

    Customer_Menu(Customer_ID)
        

    

def view_cart(Customer_ID):
    # Get the cart items for the given customer ID
    cursor.execute(f"SELECT * FROM Cart WHERE Customer_ID = {Customer_ID}")
    cart_items = cursor.fetchall()

    if not cart_items:
        print("Your cart is empty.")
        Customer_Menu(Customer_ID)

    else:
        print("Here are the items in your cart:")
        print("Product Name | Quantity | Total Price")
        total_price = 0
        for item in cart_items:
            cursor.execute(f"SELECT * FROM Product WHERE Product_ID = {item[1]}")
            prod = cursor.fetchone()
            name = prod[2]
            price = prod[4]
            quantity = int(item[2])  # Convert quantity to integer
            total_item_price = quantity * float(price)  # Convert price to integer
            total_price += total_item_price
            print(f"{name}     {quantity}     {total_item_price}")
        
        print(f"Total Price: {total_price}")

    # Ask user if they want to checkout or continue shopping
    while True:
        checkout_choice = input("Enter '1' to checkout or '2' to continue shopping: ")
        if checkout_choice.lower() == "1":
            checkout(Customer_ID)
            break
        elif checkout_choice.lower() == "2":
            Customer_Menu(Customer_ID)
            break
        else:
            print("Invalid choice. Please enter '1' to checkout or '2' to continue shopping.")

def add_to_cart():
    # Get input from user
    Customer_ID = input("Enter Customer ID: ")
    Product_ID = input("Enter Product ID: ")
    Quantity = input("Enter Quantity: ")
    Date_Of_Order = input("Enter Date of Order (YYYY-MM-DD): ")
    Cost = input("Enter Cost: ")
    Coupon_ID = input("Enter Coupon ID: ")
    Password_ = input("Enter Password: ")

    # Check if the product exists
    cursor.execute("SELECT * FROM Product WHERE Product_ID = %s", (Product_ID,))
    product = cursor.fetchone()
    if product:
        # Insert the product into the Cart table
        cursor.execute("""
            INSERT INTO Cart (Customer_ID, Product_ID, Quantity, Date_Of_Order, Cost, Coupon_ID, Password_)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """, (Customer_ID, Product_ID, Quantity, Date_Of_Order, Cost, Coupon_ID, Password_))
        mydb.commit()
        print("Product added to cart successfully!")
    else:
        print("Product not found!")


def remove_from_cart(Customer_ID):
    #global Customer_ID
    Product_ID = input("Enter the product ID you want to remove from cart: ")
    cursor = mydb.cursor()
    # Execute the query to remove the product from the cart
    query = "DELETE FROM Cart WHERE Customer_ID=%s AND Product_ID=%s"
    values = (Customer_ID, Product_ID)
    cursor.execute(query, values)
    # Commit the changes to the database
    mydb.commit()
    print("Product removed from cart successfully!")


def place_order(Customer_ID):
    checkout(Customer_ID)

def apply_coupon(Customer_ID):
    #global Customer_ID
    Coupon_ID = input("Enter the coupon code: ")
    Discount_Percentage = input("Enter the associated discount percentage with it: ")
    cursor = mydb.cursor()
    # Execute the query to apply the coupon
    query = "UPDATE Cart SET Coupon_ID=%s WHERE Customer_ID=%s"
    values = (Coupon_ID, Customer_ID)
    cursor.execute(query, values)
    # Commit the changes to the database
    mydb.commit()
    print("Coupon applied successfully!")




def rate_product(Customer_ID):
    # Get user input for rating and review
    Rating = int(input("Enter the rating (1-5): "))
    Review = input("Enter your review: ")
    
    # Execute the INSERT query with user input
    cursor = mydb.cursor()
    query = "INSERT INTO Review (Customer_ID, Rating , Review) VALUES (%s, %s, %s)"
    data = (Customer_ID, Rating, Review)
    cursor.execute(query, data)
    mydb.commit()
    print("Product rated successfully!")
    
    # Call the Customer_Menu() function
    Customer_Menu(Customer_ID)



