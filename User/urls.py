from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
   path('', views.index, name='index'),
    path('login', views.login_user, name='login'),
    path('register', views.register_user, name='register'),
    path('logout', views.logout_user, name="logout"),

    path('search/<str:search_query>', views.search_courier, name='search'),

]
