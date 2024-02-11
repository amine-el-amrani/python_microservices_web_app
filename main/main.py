from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from sqlachemy import UniqueConstraint




app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URL"] = 'mysql://root:root@db/main'
CORS(app)

db = SQLAlchemy(app)


@app.route('/')
def index():
    return 'Hello'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')