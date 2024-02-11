from flask import Flask, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate




app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql://root:root@db/main'
CORS(app)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=False) # autoincrement=False because we will create the products from the django app, so we have the same ids in both Django and Flask apps
    title = db.Column(db.String(200))
    image = db.Column(db.String(200))

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'image': self.image
        }


class ProductUser(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    product_id = db.Column(db.Integer)

    __table_args__ = (db.UniqueConstraint('user_id', 'product_id', name='user_product_unique'),)

@app.route('/api/products')
def index():
    products = Product.query.all()
    products_data = [product.to_dict() for product in products]
    return jsonify(products_data)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')