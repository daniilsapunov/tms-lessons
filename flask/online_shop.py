from dataclasses import dataclass
from flask import sql_request

from flask import Flask, abort, redirect, session, request
from flask_session import Session
import sqlite3

DATABASE_FILE = 'db.sql'

app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


@dataclass
class Category:
    id: int
    name: str


@dataclass
class Product:
    id: int
    name: str
    description: str
    favorites: str
    category_id: int


@dataclass
class User:
    user_id: int
    username: str
    password: str


def load_product_order_by_categories() -> list:
    """ Return list(product_id, product_name, description, category_id, category.name"""
    with sqlite3.connect(DATABASE_FILE) as connection:
        execute = connection.execute('''SELECT product.id, product.name, description, category_id, category.name
                                              FROM product INNER JOIN category ON product.category_id == category.id
                                              ORDER BY category.id''')
        return execute.fetchall()


def load_favorites():
    with sqlite3.connect(DATABASE_FILE) as connection:
        execution_result = connection.execute(
            'SELECT id, name, description,favorites, category_id FROM product WHERE favorites <> "" ')
        return [Product(*values) for values in execution_result.fetchall()]


def load_favorites_cat(category_id):
    with sqlite3.connect(DATABASE_FILE) as connection:
        execution_result = connection.execute(
            'SELECT id, name, description,favorites, category_id FROM product WHERE category_id = ?', (category_id,))
        return [Product(*values) for values in execution_result.fetchall()]


def load_products() -> list[Product]:
    with sqlite3.connect(DATABASE_FILE) as connection:
        execution_result = connection.execute(
            'SELECT id, name, description,favorites, category_id FROM product')
        return [Product(*values) for values in execution_result.fetchall()]


def get_category(category_id) -> Category:
    with sqlite3.connect(DATABASE_FILE) as connection:
        execution_result = connection.execute('SELECT id, name FROM category WHERE id = ?', (category_id,))
        rows = execution_result.fetchall()
        if len(rows) != 1:
            raise ValueError(f'Expected 1 object with id {category_id}, got {len(rows)}')
        return Category(*rows[0])


def get_product(product_id) -> Product:
    with sqlite3.connect(DATABASE_FILE) as connection:
        execution_result = connection.execute('SELECT id, name,description,favorites, category_id '
                                              'FROM product '
                                              'WHERE id = ?', (product_id,))
        rows = execution_result.fetchall()
        if len(rows) != 1:
            raise ValueError(f'Expected 1 object with id {product_id}, got {len(rows)}')
        return Product(*rows[0])


@app.route('/products/favorites')
def generate_html_list() -> str:
    favorites = load_favorites()
    favorites_html = '\n'.join(
        f'<li><a href="/product/{favorite.id}">{favorite.name}</a></li>'
        for favorite in favorites)

    return f'''
    <html>
        <head>
            <title>Articles APP</title>
            <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@3.4.1/dist/css/bootstrap.min.css" integrity="sha384-HSMxcRTRxnN+Bdg0JdbxYKrThecOKuH5zCYotlSAcp1+c8xmyTe9GYg1l9a69psu" crossorigin="anonymous">
        </head>
        <body>
            <a href="/products">Main page </a>
            <h1>All Products</h1>
            <ul>
                {favorites_html}
            </ul>
        </body>
    </html>'''


def add_into_favorite(product: Product):
    with sqlite3.connect(DATABASE_FILE) as connection:
        data = (product.name, product.description, product.favorites, product.id)
        connection.execute('UPDATE product'
                           ' SET name = ?, description = ?, favorites = ?'
                           ' WHERE id = ?', (data))


@app.route('/products')
def articles_view():
    products = load_products()
    products_html = '\n'.join(
        f'<li><a href="/product/{product.id}">{product.name}</a></li>'
        for product in products)

    return f'''
    <html>
        <head>
            <title>Articles APP</title>
            <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@3.4.1/dist/css/bootstrap.min.css" integrity="sha384-HSMxcRTRxnN+Bdg0JdbxYKrThecOKuH5zCYotlSAcp1+c8xmyTe9GYg1l9a69psu" crossorigin="anonymous">
        </head>
        <body>
            <h1>All Products</h1>
            <ul>
                {products_html}
            <a href=/products/favorites> Your favorites </a>
            </ul>
        </body>
    </html>'''


@app.route('/product/<int:product_id>')
def product_view(product_id: int):
    try:
        product = get_product(product_id)
    except ValueError as e:
        abort(404, e)

    return f'''
    <html>
        <head>
            <title>Product APP</title>
            <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@3.4.1/dist/css/bootstrap.min.css" integrity="sha384-HSMxcRTRxnN+Bdg0JdbxYKrThecOKuH5zCYotlSAcp1+c8xmyTe9GYg1l9a69psu" crossorigin="anonymous">
        </head>
        <body>
            <a href="/products">Main page </a>
            <h1>{product.name}</h1>
            <h3> {product.description}</h3>
            <p>favorite: {product.favorites}</p>
            <form method="post" action="/product/favorites">
            <input type="hidden" name="product_id" value="{product.id}"/>
            <input type="submit" value="Добавить в избранное"/>
            </form>
        </body>
    </html>
    '''


@app.route('/product/favorites', methods=['POST'])
def product_favorite():
    product_id = int(request.form['product_id'])
    product = get_product(product_id)
    product_favorites = session.setdefault('product_favorites', set())
    if product.id in product_favorites:
        product.favorites = ''
        product_favorites.remove(product.id)
        add_into_favorite(product)
    else:
        product.favorites = '&#10027'
        product_favorites.add(product.id)
        add_into_favorite(product)
    return redirect(f'/product/{product.id}')


# <a href=/category/{category}> Такая же категория </a>
@app.route('/category/<int:category_id>')
def category_info(category_id: int):
    try:
        category = get_category(category_id)
        products = load_favorites_cat(category_id)
        products_html = '\n'.join(
            f'<li><a href="/product/{product.id}">{product.name}</a></li>'
            for product in products)

    except ValueError as e:
        abort(404, e)

    return f'''
    <html>
        <head>
            <title>Category APP</title>
            <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@3.4.1/dist/css/bootstrap.min.css" integrity="sha384-HSMxcRTRxnN+Bdg0JdbxYKrThecOKuH5zCYotlSAcp1+c8xmyTe9GYg1l9a69psu" crossorigin="anonymous">
        </head>
        <body>
        <a href="/products">Main page </a> </br>
        <h3>Category: {category.name}</h3>
        <ul>
            {products_html}
        </ul>
        </body>
    </html>
    '''


@app.route('/')
def main_page():
    full = load_product_order_by_categories()
    products_html = '\n'.join(
        f'<br>'
        f'<a href="/product/{product[0]}">{product[1]}</a></li>'
        for product in full)

    return f'''
    <html>
        <head>
            <title>Articles APP</title>
            <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@3.4.1/dist/css/bootstrap.min.css" integrity="sha384-HSMxcRTRxnN+Bdg0JdbxYKrThecOKuH5zCYotlSAcp1+c8xmyTe9GYg1l9a69psu" crossorigin="anonymous">
        </head>
        <body>
            <h1>All Products</h1>
            <ul>
            <li>Category: <a href="/category/{full[0][3]}">{full[2][2]}</a></li>
                    <a href="/product/{full[0][0]}">{full[0][1]}</a></li><br>
                    <a href="/product/{full[1][0]}">{full[1][1]}</a></li><br>
                    <a href="/product/{full[2][0]}">{full[2][1]}</a></li><br>
            <li>Category: <a href="/category/{full[3][3]}">{full[3][2]}</a></li>
                    <a href="/product/{full[3][0]}">{full[3][1]}</a></li><br>
                    
            <a href=/products/favorites> Your favorites </a>
            </ul>
        </body>
    </html>'''


if __name__ == '__main__':
    app.run(port=8081, debug=True)
