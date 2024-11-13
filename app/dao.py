# Data Access Object
# Dùng để đọc các file json
import json
from keyword import kwlist

from app import app
from app.models import Category, Product , User
import hashlib


def load_categories():
    #Này đọc JSON không dùng trong đồ án
    # cần truyền đường dẫn tuyệt đối để app nào cũng chạy được
    # with open('%s/data/categories.json' % app.root_path, encoding='utf-8') as f:
    #     return json.load(f)

    #Này đọc dữ liệu từ MYSQL
    #Câu lệnh này tương đương SELECT * trong CSDl
    return Category.query.all()


def load_products(cate_id=None , kw =None):
    # with open('%s/data/products.json' % app.root_path, encoding='utf-8') as f:
    #     products = json.load(f)
    #     if cate_id:
    #         # Nhớ chuyển dữ liệu cate_id về số
    #         products = [p for p in products if p['category_id'] == int(cate_id)]
    #     return products

    query = Product.query
    if cate_id:
        query = query.filter(Product.category_id.__eq__(cate_id))
    if kw:
        # Tương đương với mênh đề WHERE LIKE
        # nó sẽ lấy kw bên của index.py
        query = query.filter(Product.name.contains(kw))
    return  query.all()
#Lấy id product
def get_product_by_id(product_id):
    # lấy product_id dưới CSDL
    return Product.query.get(product_id)

#Cho người dùng nhập mật khẩu
#Strip() cắt khoảng trắng 2 đầu
def auth_user(username , password):
    password = str(hashlib.md5(password.strip().encode('utf-8')).digest()) #nữa dùng .hexdigest()
    return User.query.filter(User.username.__eq__(username.strip()), User.password.__eq__(password)).first()
def get_user_id(user_id):
    return User.query.get(user_id)