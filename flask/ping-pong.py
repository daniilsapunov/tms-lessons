from dataclasses import dataclass

from flask import Flask,abort,request

import sqlite3

app = Flask(__name__)

@app.route('/')
@app.route('/ping')
def ping():
    return f'''
    <html>
        <head>
            <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@3.4.1/dist/css/bootstrap.min.css" integrity="sha384-HSMxcRTRxnN+Bdg0JdbxYKrThecOKuH5zCYotlSAcp1+c8xmyTe9GYg1l9a69psu" crossorigin="anonymous">
        </head>
        <body>
        <h1><a href="/pong">Pong</a></h1>
        </body>
    </html>
    '''
@app.route('/pong')
def pong():
    return f'''
    <html>
        <head>
            <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@3.4.1/dist/css/bootstrap.min.css" integrity="sha384-HSMxcRTRxnN+Bdg0JdbxYKrThecOKuH5zCYotlSAcp1+c8xmyTe9GYg1l9a69psu" crossorigin="anonymous">
        </head>
                <body>
        <h1><a href="/ping">Ping</a></h1>
        </body>
    </html>
    '''


if __name__ == '__main__':
    app.run(port=8080, debug=True)
