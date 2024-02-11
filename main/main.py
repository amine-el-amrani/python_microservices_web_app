from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from sqlachemy import UniqueConstraint




app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URL"] = 'mysql://root:root@db/main'
CORS(app)

db = SQLAlchemy(app)


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=False) # autoincrement=False because we will create the products from the django app, so we have the same ids in both Django and Flask apps
    title = db.column(db.String(200))
    image = db.column(db.String(200))


class ProdictUser(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    product_id = db.Column(db.Integer)


    UniqueConstraint('user_id', 'product_id', name='user_product_unique')

@app.route('/')
def index():
    return 'Hello'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')