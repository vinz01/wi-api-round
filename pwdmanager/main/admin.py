from django.contrib import admin

# Register your models here.
from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path("app/user", views.register, name="register"),
    # 
    # path("logout", views.logout_request, name="logout"),
    # path("login", views.login_request, name="login"),
    # path("app/sites/list/<str:userid>/", views.list, name="list"),
    # path("app/sites/<str:userid>/", views.addsite, name="addsite")
]