# import các models quản lý vào
from django.contrib.auth import authenticate

from app.models import Category , Product
from app import db , app
from flask_admin import Admin ,BaseView , expose
from flask_admin.contrib.sqla import ModelView
from flask_login import current_user
# pip install flask-admin


#Class này ghi đè lại admin của ModelView
class ProductView(ModelView):
    #tên category sẽ tủng với tên của backref='category'
    column_list = ['id','name' , 'price' ,'category']
    column_searchable_list = ['name']
    column_filters = ['name','price']
    can_view_details = True
    can_export = True
    # Khong hien thi
    column_export_list = ['image']

    column_labels = {
        'name' :'Tên sản phẩm',
        'description' :'Mô tả',
        'price' : 'Giá',
        'active' :'Trạng thái'}
    # Mục sản phẩm chỉ được xuất hiện khi chưng
    def is_accessible(self):
        return current_user.is_authenticated

class CategoryView(ModelView):
    # truyền đúng tên products -> truyền như vậy mới Edit đc Category với hiện danh sách sản phẩm trong  1 Danh mục
    column_list = ['id','name','products']
    can_view_details = True



# Thống kê báo cáo
class StatsView(BaseView):
    @expose('/')
    def __index__(self):
        return self.render(('admin/stats.html'))


admin = Admin(app=app , name='Quản trị bán hàng' , template_mode='bootstrap4')
# Thêm các models muốn quản trị
admin.add_view(CategoryView(Category , db.session , name='Danh mục'))
admin.add_view(ProductView(Product , db.session , name='Sản phẩm'))
admin.add_view((StatsView(name='Thống kê')))



#Làm xong nhớ import vào bên index.py