from django.urls import path
from . import views

urlpatterns=[
    path("",views.log),
    path("admin_home",views.admin_home),
    path("logout",views.admin_logout),
    path("add",views.add_pro),

    # user registration

    path("registration",views.reg),
    path("userhome",views.user_home),
    path("view_product/<pid>",views.view_product),
    path("add_to_cart/<pid>",views.add_to_cart),
    path("view_cart",views.view_cart),
    
]