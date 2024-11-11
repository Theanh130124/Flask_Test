from flask import render_template ,request
from unicodedata import category

from app import app # sau khi đã refactor qua bên init
from app import dao


# __name__ nó sẽ tự hieu là tên của package python
@app.route('/') # @saleapp nếu như saleapp = Flask(...)
def index():
    # return  'hello the anh'
    cate_id = request.args.get('category_id')
    # Sau khi viết cate_id thì qua bên dao.py truyền vào load_product
    categories = dao.load_categories()
    products = dao.load_products(cate_id)
    return  render_template('index.html' , categories = categories , products =products) #nó sẽ tự động tìm trong templates
#categories red là biến dùng ngoài templates -> nghĩa là trên index nó dùng ,  còn màu trắng là biến = dao.load_categories



if __name__ == '__main__':
    app.run(debug=True, port =5001) #port này thêm vào để làm port của /
