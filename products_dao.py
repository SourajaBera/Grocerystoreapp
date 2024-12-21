import MySQLdb

def connect_to_db():
    connection = MySQLdb.connect(
        host="localhost",
        user="root",
        passwd="sourajabera@2002",
        db="grocery"
    )
    return connection


def add_product(name, price, stock):
    conn = connect_to_db()
    cursor = conn.cursor()
    query = "INSERT INTO products (name, price, stock) VALUES (%s, %s, %s)"
    cursor.execute(query, (name, price, stock))
    conn.commit()
    print("Product added successfully!")
    conn.close()
def view_products():
    conn = connect_to_db()
    cursor = conn.cursor()
    query = "SELECT * FROM products"
    cursor.execute(query)
    for row in cursor.fetchall():
        print(row)
    conn.close()
def update_stock(product_id, new_stock):
    conn = connect_to_db()
    cursor = conn.cursor()
    query = "UPDATE products SET stock = %s WHERE id = %s"
    cursor.execute(query, (new_stock, product_id))
    conn.commit()
    print("Stock updated successfully!")
    conn.close()
def delete_product(product_id):
    conn = connect_to_db()
    cursor = conn.cursor()
    query = "DELETE FROM products WHERE id = %s"
    cursor.execute(query, (product_id,))
    conn.commit()
    print("Product deleted successfully!")
    conn.close()
def main():
    while True:
        print("\n1. Add Product")
        print("2. View Products")
        print("3. Update Stock")
        print("4. Delete Product")
        print("5. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            name = input("Enter product name: ")
            price = float(input("Enter price: "))
            stock = int(input("Enter stock quantity: "))
            add_product(name, price, stock)
        elif choice == "2":
            view_products()
        elif choice == "3":
            product_id = int(input("Enter product ID: "))
            new_stock = int(input("Enter new stock quantity: "))
            update_stock(product_id, new_stock)
        elif choice == "4":
            product_id = int(input("Enter product ID: "))
            delete_product(product_id)
        elif choice == "5":
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()