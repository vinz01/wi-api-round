from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path("app/user", views.register, name="register"),
    path("app/", views.home, name="home"),
    path("app/user/auth", views.login, name="login"),
    # # path("logout", views.logout_request, name="logout"),
    # # path("login", views.login_request, name="login"),
    path("app/sites/list/<str:userid>/", views.list, name="list"),
    path("app/sites/<str:userid>/", views.addsite, name="addsite"),
    path("app/panel", views.panel, name="panel"),
]