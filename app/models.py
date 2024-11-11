from sqlalchemy import Column ,INTEGER,String
from flask_sqlalchemy import SQLAlchemy
from app import db ,app


class Category(db.Model):
    # Chỉ định tên bản tự tạo
    __tablename__ = 'category'
    id = Column(INTEGER ,primary_key=True , autoincrement=True)
    name =Column(String(50), nullable=False , unique=True)
if __name__ == "__main__":
    with app.app_context():
        db.create_all()


