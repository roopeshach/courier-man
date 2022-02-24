from django.shortcuts import render, redirect
from .models import Courier
from .forms import CourierForm
from django.contrib.auth.mixins import LoginRequiredMixin  , UserPassesTestMixin
from django.views.generic.edit import UpdateView , CreateView
from django.views.generic import ListView, DetailView
from django.utils import timezone
# Create your views here.
#listview for courier
class CourierListView(LoginRequiredMixin , ListView):
    model = Courier
    template_name = 'Delivery/couriers.html'
    context_object_name = 'couriers'
    ordering = ['-created_at']
    def get_queryset(self):
        return Courier.objects.all()

#detailview for courier
class CourierDetailView(LoginRequiredMixin , DetailView):
    model = Courier
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


class  CourierView ( LoginRequiredMixin, UserPassesTestMixin, CreateView):

    def test_func(self):
        login_url = '/login/'
        return(self.request.user)

    
    def get(self,request):
        
        couriers = Courier.objects.filter(user=self.request.user)
        context = {
            'couriers': couriers,
        }
        return render(request, 'Delivery/courier.html', context)
    
    def post(self, request):
        courier_form = CourierForm(request.POST , request.FILES)
        context = {
            'courier_form' : CourierForm,
        }

        if courier_form.is_valid():
            courier_form.save()
            return redirect('Delivery:courier')
        else:
            print(courier_form.errors)
            return render(request, 'Delivery/couriers.html', context)
  
        
        return redirect('Delivery:courier')

def delete_courier(request , id):
    Courier.objects.get(id=id).delete()
    render(request , 'Delivery/courier.html' , {'response' : "Courier deleted successfully"})
    return redirect('Delivery:courier')

class UpdateCourier( UpdateView):

    def test_func(self):
        login_url  = 'login/'
        return(self.request.user)
    
    model = Courier

    fields = ('__all__')
