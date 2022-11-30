from django.urls import path
from . import views
urlpatterns = [
    path('', views.index,name="index"),
    path('register/', views.regi,name="register"),
    path('login/', views.log,name="login"),
    path('logout/', views.logout,name="logout"),


]