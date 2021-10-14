
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('home',views.index,name="home"),
    path('accounts/sign_up/',views.sign_up,name="sign-up"),
    path('login/',views.loginPage,name="login"),
    path('logout/',views.logout,name="logout")
]
