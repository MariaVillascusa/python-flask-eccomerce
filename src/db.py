import pymysql

mysql = pymysql.connect(host='localhost', port=3306,
                        user='user', passwd='user', database='flask-ecommerce')
# host='127.0.0.1' ??