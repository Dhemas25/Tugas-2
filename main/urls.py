from django.urls import path
from main.views import show_main,create_product, show_xml, show_json, show_xml_by_id, show_json_by_id, register, login_user, logout_user
from main.views import add1_to_inventory,delete_item,remove1_from_inventory, edit_product,get_product_json,add_product_ajax
from main.views import create_product_flutter

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-product', create_product, name='create_product'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'), 
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'), 
    path('register/', register, name='register'), 
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('add1-to-inventory/<int:id>/', add1_to_inventory, name='add1_to_inventory'),
    path('remove1-from-inventory/<int:id>/', remove1_from_inventory, name='remove1_from_inventory'),
    path('delete-item/<int:id>/', delete_item, name='delete_item'),
    path('edit-product/<int:id>', edit_product, name='edit_product'),
    path('get-product/', get_product_json, name='get_product_json'),
    path('create-product-ajax/', add_product_ajax, name='add_product_ajax'),
    path('create-flutter/', create_product_flutter, name='create_product_flutter'),
]
