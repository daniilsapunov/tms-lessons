import sqlite3
DATABASE_FILE = 'db.sql'

def create_table():
    with sqlite3.connect('db.sql') as connection:
        result = connection.execute("""
        CREATE TABLE IF NOT EXISTS product  (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name VARCHAR UNIQUE,
            description VARCHAR,
            category_id VARCHAR,
            FOREIGN KEY(category_id) REFERENCES category(id)
            );""")


def add_products(name, description):
    with sqlite3.connect('db.sql') as connection:
        result = connection.execute("""
        INSERT INTO product(name, description)
        VALUES(?,?)
        ;""", (name, description))


def create_category():
    with sqlite3.connect('db.sql') as connection:
        result = connection.execute("""
        CREATE TABLE IF NOT EXISTS category  (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name VARCHAR
            );""")


def drop_products():
    with sqlite3.connect('db.sql') as connection:
        result = connection.execute("""
        DROP TABLE category""")


def drop_category():
    with sqlite3.connect('db.sql') as connection:
        result = connection.execute("""
        DELETE FROM category WHERE id = 4""")


def update_favorites():
    with sqlite3.connect('db.sql') as connection:
        execution_result = connection.execute(
            'UPDATE product, category '
            'SET product.category_id = category.id'
            'WHERE product.description = category.name  '
            'AND product.category_id = 0')


def update_categoryy():
    with sqlite3.connect('db.sql') as connection:
        execution_result = connection.execute(
            'UPDATE product SET category_id = 2 WHERE description = "vintage" ')


def get_product():
    with sqlite3.connect('db.sql') as connection:
        result = connection.execute("""SELECT * FROM product""")
    return result.fetchall()

def load_product_order_by_categories() -> list:
    """ Return list(product_id, product_name, description, category_id, category.name"""
    with sqlite3.connect(DATABASE_FILE) as connection:
        execute = connection.execute('''SELECT product.id, product.name, description, category_id
                                              FROM product INNER JOIN category ON product.category_id == category.id
                                              ORDER BY category.id''')
        return execute.fetchall()

def get_category():
    with sqlite3.connect('db.sql') as connection:
        result = connection.execute("""SELECT * FROM category""")
    return result.fetchall()


def add_foreign_key():
    with sqlite3.connect('db.sql') as connection:
        execution_result = connection.execute(
            'ALTER TABLE product ADD FOREIGN KEY(category_id) REFERENCES category(id)')


def add_product_favorites():
    with sqlite3.connect('db.sql') as connection:
        execution_result = connection.execute(
            'ALTER TABLE category RENAME COLUMN name VARCHAR UNIQUE  ')


def update_category(name):
    with sqlite3.connect('db.sql') as connection:
        result = connection.execute("""
        INSERT INTO product(product_id)
        VALUES(?)
        WHERE description = 'premium'
        ;""", (name,))

#add_product_favorites()
#print(get_product())
#print(get_category())

#('bmw m5 f90, 4.4','premium')
#add_products('BMW 7-Series 760i xDrive, 4.4','premium')
#add_products('Mercedes-AMG GT, 4.0','premium')
#add_products('Nissan GT-R Track Edition, 3.8','vintage')

#update_favorites()
#create_category()
#add_foreign_key()


print(load_product_order_by_categories())