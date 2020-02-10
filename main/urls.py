from django.contrib import admin
from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name="index"),
    path('login/', views.login_request, name="login"),
    path("logout/", views.logout_request, name="logout"),
    path('demo/', views.demo, name="demo"),
    path('account/', views.account, name="account"),
    path('code/', views.code, name="code"),

]
