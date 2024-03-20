import mysql.connector
import json

connection = mysql.connector.connect(
    user='root', password='root', host='mysql', port="3306", database='db')
print("DB connected")

create_table_query = """
    CREATE TABLE IF NOT EXISTS products (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255),
        price DECIMAL(10, 2),
        brand VARCHAR(255),
        image_url VARCHAR(255),
        product_url VARCHAR(255)
    )
"""

try:
    cursor = connection.cursor()
    cursor.execute(create_table_query)
    print("Table created successfully.")
except Exception as e:
    print(f"Error creating table: {e}")

json_file = "products.json"

with open(json_file, 'r') as file:
    product_data = json.load(file)

insert_query = """
    INSERT INTO products (name, price, brand, image_url, product_url)
    VALUES (%s, %s, %s, %s, %s)
"""
try:
    for product in product_data:
        name = product['Name']
        price = product['Price']
        brand = product['Brand']
        image_url = product['Image URL']
        product_url = product['Product URL']
        
        cursor.execute(insert_query, (name, price, brand, image_url, product_url))
    
    connection.commit()

    print("Data inserted successfully.")
    select_query = "SELECT * FROM products"
    cursor.execute(select_query)
    products = cursor.fetchall()

    print("Inserted data:")
    for product in products:
        print(product)

except Exception as e:
    print(f"Error: {e}")
    connection.rollback()
finally:
    cursor.close()
    connection.close()
