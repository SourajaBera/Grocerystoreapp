
USE grocery;INSERT INTO orders (id, product_id, quantity)
VALUES (
    id:int,
    product_id:int,
    quantity:int
  );
CREATE TABLE products (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    price FLOAT NOT NULL,
    stock INT NOT NULL  
);
INSERT INTO products (name, price, stock) VALUES ('Apple', 1.5, 100);

CREATE TABLE orders (
    id INT AUTO_INCREMENT PRIMARY KEY,
    product_id INT NOT NULL,
    quantity INT NOT NULL,
    FOREIGN KEY (product_id) REFERENCES products(id)
);
