from django.urls import path
from . import views

urlpatterns=[
    path("",views.log),
    path("admin_home",views.admin_home),
    path("registration",views.reg),
]