from itertools import product
from flask import request, render_template, redirect, flash
from flask.views import MethodView
from src.db import mysql


class IndexController(MethodView):
    def get(self):
        with mysql.cursor() as cur:
            cur.execute('SELECT * FROM products')
            products = cur.fetchall()
            cur.execute('SELECT * FROM categories')
            categories = cur.fetchall()
        return render_template('public/index.html', products=products, categories=categories)

    def post(self):
        code = request.form['code']
        name = request.form['name']
        stock = request.form['stock']
        value = request.form['value']
        category = request.form['category']

        with mysql.cursor() as cur:
            try:
                cur.execute(
                "INSERT INTO products(code, name, stock, value, id_category) VALUES(%s, %s, %s, %s, %s)", (code, name, stock, value, category))
                cur.connection.commit()
                flash('El producto ha sido creado correctamente', 'success')
            except:
                flash('Ha ocurrido un error', 'error')

            return redirect('/')


class DeleteProductController(MethodView):
    def post(self, code):
        with mysql.cursor() as cur:
            cur.execute(
                'DELETE FROM products WHERE code = %s', (code))
            cur.connection.commit()
            return redirect('/')


class UpdateProductController(MethodView):
    def get(self, code):
        with mysql.cursor() as cur:
            cur.execute(
                'SELECT * FROM products WHERE code = %s', (code))
            product = cur.fetchone()
            return render_template('/public/update.html', product=product)

    def post(self, code):
        productCode = request.form['code']
        name = request.form['name']
        stock = request.form['stock']
        value = request.form['value']
        category = request.form['category']

        with mysql.cursor() as cur:
            cur.execute(
                "UPDATE products SET code = %s, name = %s, stock = %s, value = %s WHERE code = %s", (productCode, name, stock, value, code))
            cur.connection.commit()

        return f'Editing product {code} works'


class CreateCategoriesController(MethodView):
    def get(self):
        return render_template('/public/categories.html')

    def post(self):
        id = request.form['id']
        name = request.form['name']
        description = request.form['description']
        
        with mysql.cursor() as cur:
            try:
                cur.execute(
                    "INSERT INTO categories(id, name, description) VALUES(%s, %s, %s)", (id, name, description))
                cur.connection.commit()
                flash('Nueva categoría creada', 'success')
            except:
                flash('Ha ocurrido un error', 'error')
            return redirect('/')

