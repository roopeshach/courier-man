from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
   path('', views.index, name='index'),
    path('login', views.login_user, name='login'),
    path('register', views.register_user, name='register'),
    path('logout', views.logout_user, name="logout"),
    path('reset-password', views.reset_user_password, name="reset-password"),
    path('verify-otp/<int:id>', views.verify_otp, name="verify-otp"),
    path('change-password/<int:id>', views.change_password, name="change-password"),
    path('users', views.users_list, name='users'),
    path('toggle-user-active/<int:id>', views.toggle_user_active, name='toggle_user_active'),
    path('toggle-user-admin/<int:id>', views.toggle_user_admin, name='toggle_user_admin'),

    path('search/<str:search_query>', views.search_courier, name='search'),

]
