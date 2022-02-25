from django.urls import path
from . import views
urlpatterns = [
    path('customer', views.index, name='index'),
    path('customer-couriers', views.CourierListView.as_view(), name='courier_list_customer'),
    path('customer-courier', views.CourierView.as_view(), name='courier_customer'),
]
