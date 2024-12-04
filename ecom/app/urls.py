from django.urls import path
from . import views

urlpatterns=[
    # admin

    path("",views.log),
    path("admin_home",views.admin_home),
    path("logout",views.admin_logout),
    path("add",views.add_pro),
    path("view_bookings",views.view_bookings),
    path('user_view',views.admin_user_view),

    # user 

    path("registration",views.reg),
    path("userhome",views.user_home),
    path("view_product/<pid>",views.view_product),
    path("add_to_cart/<pid>",views.add_to_cart),
    path("view_cart",views.view_cart),
    path('qty_in/<cid>',views.qty_in),  
    path('qty_dec/<cid>',views.qty_dec),
    path('cart_pro_buy/<cid>',views.cart_pro_buy),
    path('bookings',views.bookings),
    path('pro_buy/<pid>',views.pro_buy),
]
    
