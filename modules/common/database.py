import sqlite3


class Database():

    def __init__(self):
        self.connection = sqlite3.connect(r'C:\Users\iserp\qa_auto\prometheus_qa_auto' + r'\become_qa_auto.db')
        self.cursor = self.connection.cursor()

    def test_connection(self):
        sqlite_select_query = 'SELECT sqlite_version();'
        self.cursor.execute(sqlite_select_query)
        record = self.cursor.fetchall()
        print(f'Connected successfully. SQLite Database Version is: {record}')

    def get_all_users(self):
        query = 'SELECT name, address, city FROM customers'
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record
    
    def get_user_address_by_name(self, name):
        query = f"SELECT address, city, postalCode, country FROM customers WHERE name = '{name}'"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record

    def update_product_qnt_by_id(self, product_id, qnt):
        query = f"UPDATE products SET quantity = {qnt} WHERE id = {product_id}"
        self.cursor.execute(query)
        self.connection.commit()
    
    def select_product_qnt_by_id(self, product_id):
        query = f"SELECT quantity FROM products WHERE id = {product_id}"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record
    
    def insert_product(self, product_id, name, description, qnt):
        query = f"INSERT OR REPLACE INTO products (id, name, description, quantity) \
            VALUES ({product_id}, '{name}', '{description}', {qnt})"
        self.cursor.execute(query)
        self.connection.commit()

    def delete_product_by_id(self, product_id):
        query = f"DELETE FROM products WHERE id in ({product_id})"
        self.cursor.execute(query)
        self.connection.commit()
    
    def get_detailed_orders(self):
        query = "SELECT o.id, c.name, p.name, \
                p.description, o.order_date \
                FROM orders as o \
                JOIN customers as c ON o.customer_id = c.id \
                JOIN products as p ON o.product_id = p.id"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record
    
    def pure_insert_product(self, product_id, name, description, qnt):
        """Method for pure inserting data to products table"""

        query = f"INSERT INTO products (id, name, description, quantity) \
                VALUES ({product_id}, '{name}', '{description}', {qnt})"
        try:
            self.cursor.execute(query)
            self.connection.commit()
        except sqlite3.IntegrityError:
            print('An error occurred while inserting data')
     
    def select_count_product_by_id(self,id):
        """Method for calculation count of given product in products table"""

        query = f"SELECT count(id) from products WHERE id = {id}"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record
    
    def create_table_order_details(self):
        """Method creates order_details table"""

        query = 'CREATE TABLE IF NOT EXISTS order_details ( \
                id INT PRIMARY KEY  NOT NULL, \
                order_id INT NOT NULL, \
                amount INT NOT NULL, \
                FOREIGN KEY(order_id) REFERENCES orders(id) \
                );'
        self.cursor.execute(query)
        self.connection.commit()
    
    def select_name_from_sqlite_schema(self):
        """Method retrieves names of existing tables in SQLite DB"""

        query = 'SELECT name FROM sqlite_schema;'
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record
    
    def insert_order_details(self, id, order_id, amount):
        """Method inserts data into order_details table"""

        query = f"INSERT OR REPLACE INTO order_details (id, order_id, amount) \
                VALUES ({id}, {order_id}, {amount});"
        self.cursor.execute(query)
        self.connection.commit()
    
    def select_order_details(self):
        """Method for retrieving data from order_details table"""

        query = "SELECT id, order_id, amount FROM order_details;"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record
    
    def drop_order_details_table(self):
        """Method for deleting of order_details table from database"""

        query = "DROP TABLE order_details;"
        self.cursor.execute(query)
        self.connection.commit()

    def select_min_max_avg_product_qty(self,operand):
        """Method for calculation min, max or avg of products quantity"""

        query = ""
        if operand == 'min':
            query = "SELECT min(quantity) FROM products;"
        elif operand == 'max':
            query = "SELECT max(quantity) FROM products;"
        elif operand == 'avg':
            query = "SELECT round(avg(quantity),0) FROM products;"
        else:
            print("Invalid operand, please use 'min' or 'max' or 'avg'")

        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record
    
    def select_product_with_max_description(self):
        """Method for selecting product description with maximum length"""

        query = "SELECT description, \
                length(description) as len \
                FROM products \
                ORDER BY len DESC \
                LIMIT 1;"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record
    
    def insert_customers(self):
        """Method for inserting data to customers table"""

        query = "INSERT OR REPLACE INTO customers \
                VALUES (3, 'Petro', 'Nebesnoi sotni, 33', 'Odesa', '65012', 'Ukraine'), \
                (4, 'Alina', 'Shevchenko, 12', 'Odesa', '65122', 'Ukraine'), \
                (5, 'Nastia', 'Derebasivska, 15', 'Odesa', '65312', 'Ukraine'), \
                (6, 'Leonid', 'Myru, 52', 'Izmail', '68014', 'Ukraine'), \
                (7, 'Svetlana', 'Nezalezhnosti, 3', 'Izmail', '68017', 'Ukraine'), \
                (8, 'Oleg', 'Lesi Ukrayinky, 16', 'Bucha', '08292', 'Ukraine');"
        self.cursor.execute(query)
        self.connection.commit()

    def select_customers_city_max_count(self):
        """Method for counting which city most appears in customers table"""

        query = "SELECT city, count(city) as cnt \
                FROM customers \
                GROUP BY city \
                ORDER BY cnt DESC \
                LIMIT 1;"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record

    def insert_into_orders(self):
        """Method for inserting data into orders table"""
        
        query = "INSERT INTO orders (id, customer_id, product_id) \
                VALUES (2, 3, 3), \
                (3, 4, 4), \
                (4, 5, 5), \
                (5, 6, 6), \
                (6, 7, 6), \
                (7, 5, 6), \
                (8, 3, 6);"
        self.cursor.execute(query)
        self.connection.commit()

    def delete_from_orders(self):
        """Method for deleting from orders table"""
        
        query = "DELETE FROM orders \
                WHERE id <> 1;"
        self.cursor.execute(query)
        self.connection.commit()

    def select_bestseller(self):
        """Method for selecting the best selling product"""
        
        query = "SELECT p.name, count(o.product_id) as qnt \
                FROM orders o \
                JOIN products p ON o.product_id = p.id \
                GROUP BY o.product_id \
                ORDER BY qnt DESC \
                LIMIT 1;"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record
    