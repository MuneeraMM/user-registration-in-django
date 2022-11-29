from django.urls import path
from . import views
urlpatterns = [
    path('', views.index,name="index"),
    path('register/', views.regi,name="regis"),
    path('login/', views.log,name="logi"),

]