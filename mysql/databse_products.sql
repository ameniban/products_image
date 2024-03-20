USE db;

CREATE TABLE products (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    price DECIMAL(10, 2),
    brand VARCHAR(255),
    image_url VARCHAR(255),
    product_url VARCHAR(255)
);

