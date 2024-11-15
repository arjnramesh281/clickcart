from django.urls import path
from . import views

urlpatterns=[
    path("",views.log),
    path("admin_home",views.admin_home),
    path("logout",views.admin_logout),
    path("add",views.add_pro),
    path("registration",views.reg),
]