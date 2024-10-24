# Data Access Object
# Dùng để đọc các file json
import json

from app import app


def load_categories():
    # cần truyền đường dẫn tuyệt đối để app nào cũng chạy được
    with open('%s/data/categories.json' % app.root_path, encoding='utf-8') as f:
        return json.load(f)


def load_products(cate_id=None):
    with open('%s/data/products.json' % app.root_path, encoding='utf-8') as f:
        products = json.load(f)
        if cate_id:
            # Nhớ chuyển dữ liệu cate_id về số
            products = [p for p in products if p['category-id'] == int(cate_id)]
        return products
