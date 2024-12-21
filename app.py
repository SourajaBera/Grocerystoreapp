from flask import Flask, render_template, request, redirect, url_for
import MySQLdb

app = Flask(__name__)

# Database connection function
def connect_to_db():
    connection = MySQLdb.connect(
        host="localhost",
        user="root",
        passwd="sourajabera@2002",
        db="grocery"
    )
    return connection

# Route to view products
@app.route('/')
def view_products():
    conn = connect_to_db()
    cursor = conn.cursor()
    query = "SELECT * FROM products"
    cursor.execute(query)
    products = cursor.fetchall()
    conn.close()
    return render_template('view_products.html', products=products)

# Route to add a product
@app.route('/add', methods=['GET', 'POST'])
def add_product():
    if request.method == 'POST':
        name = request.form['name']
        price = request.form['price']
        stock = request.form['stock']
        
        conn = connect_to_db()
        cursor = conn.cursor()
        query = "INSERT INTO products (name, price, stock) VALUES (%s, %s, %s)"
        cursor.execute(query, (name, price, stock))
        conn.commit()
        conn.close()
        return redirect(url_for('view_products'))
    
    return render_template('add_product.html')

# Route to update stock
@app.route('/update/<int:product_id>', methods=['GET', 'POST'])
def update_stock(product_id):
    if request.method == 'POST':
        new_stock = request.form['new_stock']
        
        conn = connect_to_db()
        cursor = conn.cursor()
        query = "UPDATE products SET stock = %s WHERE id = %s"
        cursor.execute(query, (new_stock, product_id))
        conn.commit()
        conn.close()
        return redirect(url_for('view_products'))
    
    return render_template('update_stock.html', product_id=product_id)

# Route to delete a product
@app.route('/delete/<int:product_id>', methods=['POST'])
def delete_product(product_id):
    conn = connect_to_db()
    cursor = conn.cursor()
    query = "DELETE FROM products WHERE id = %s"
    cursor.execute(query, (product_id,))
    conn.commit()
    conn.close()
    return redirect(url_for('view_products'))

if __name__ == '__main__':
    app.run(debug=True)
