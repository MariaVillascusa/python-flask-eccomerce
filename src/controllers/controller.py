from flask import request, render_template, redirect
from flask.views import MethodView
from src.db import mysql

class IndexController(MethodView):
    def get(self):
        with mysql.cursor() as cur:
            cur.execute('SELECT * FROM products')
            data = cur.fetchall()
        return render_template('public/index.html', data=data)

    def post(self):
        code = request.form['code']
        name = request.form['name']
        stock = request.form['stock']
        value = request.form['value']
        category = request.form['category']

        with mysql.cursor() as cur:
            cur.execute("INSERT INTO products(code, name, stock, value) VALUES(%s, %s, %s, %s)",(code, name, stock, value))
            cur.connection.commit()
            return redirect('/')

