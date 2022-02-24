from django.urls import path
from django.contrib import admin
from . import views
urlpatterns = [
    path('courier', views.CourierView.as_view(), name='courier'),
    path('couriers', views.CourierListView.as_view(), name='couriers'),
    path('update-courier/<int:pk>', views.UpdateCourier.as_view(), name='update-courier'),
    path('delete-courier/<int:id>', views.delete_courier, name='delete-courier'),
    path('courier-detail/<int:pk>', views.CourierDetailView.as_view(), name='courier-detail'),

]
