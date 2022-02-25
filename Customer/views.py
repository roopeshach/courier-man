from django.shortcuts import render, redirect
from Delivery.models import Courier
from Delivery.forms import CourierForm
from django.contrib.auth.mixins import LoginRequiredMixin  , UserPassesTestMixin
from django.views.generic.edit import UpdateView , CreateView
from django.views.generic import ListView, DetailView
from django.utils import timezone
# Create your views here.

def index(request):
    recent_couriers = Courier.objects.order_by('-created_at').filter(user=request.user)[:3]
    courier_count = Courier.objects.filter(user=request.user).count()
    pending_couriers = Courier.objects.filter(user=request.user).filter(status='Pending').count()
    delivered_couriers = Courier.objects.filter(user=request.user).filter(status='Delivered').count()
    context = {
        'recent_couriers': recent_couriers,
        'courier_count': courier_count,
        'pending_couriers': pending_couriers,
        'delivered_couriers': delivered_couriers,

    }
    return render(request, 'Customer/index.html', context)

#listview for courier
class CourierListView(LoginRequiredMixin , ListView):
    model = Courier
    template_name = 'Delivery/couriers.html'
    context_object_name = 'couriers'
    ordering = ['-created_at']
    def get_queryset(self):
        return Courier.objects.filter(user=self.request.user)



class  CourierView ( LoginRequiredMixin, UserPassesTestMixin, CreateView):

    def test_func(self):
        login_url = '/login/'
        return(self.request.user)

    
    def get(self,request):
        
        couriers = Courier.objects.filter(user=self.request.user)
        context = {
            'couriers': couriers,
        }
        return render(request, 'Customer/courier.html', context)
    
    def post(self, request):
        courier_form = CourierForm(request.POST , request.FILES)
        context = {
            'courier_form' : CourierForm,
        }

        if courier_form.is_valid():
            courier_form.save()
            return redirect('Customer:courier')
        else:
            print(courier_form.errors)
            return render(request, 'Customer/couriers.html', context)
  
        
        return redirect('Customer:courier')


