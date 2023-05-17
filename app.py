from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import DATABASE
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = f"{DATABASE['ENGINE']}://{DATABASE['URI']}"
app.config['SQLAMCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
from routes import routes_bp
app.register_blueprint(routes_bp)

if __name__ == '__main__':
    app.run()
