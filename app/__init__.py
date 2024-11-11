from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)  # Sau khi đã refactor từ bên index
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://root:123456@localhost/flask_2'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
db = SQLAlchemy(app=app)

