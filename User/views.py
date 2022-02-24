from django.shortcuts import render, redirect
from .forms import UserForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login , logout
from django.db.models import Q
from Delivery.models import Courier
# Create your views here.

def index(request):
    if request.user.is_authenticated:
        courier_count = Courier.objects.all().count()
        users_count = User.objects.all().count()
        pending_couriers = Courier.objects.filter(status='Pending').count()

        context = {
            'courier_count': courier_count,
            'users_count': users_count,
            'pending_couriers': pending_couriers,
        }
        return render(request, 'User/index.html', context)

        

    else:
        return redirect('User:login')

##search courier by any field
def search_courier(request, search_query):
    if request.user.is_authenticated:
        
        search_query = str(search_query)
        #filter data by search query and search in all fields
        couriers = Courier.objects.filter(
        Q(status__icontains=search_query) |
        Q(user__username__icontains=search_query) |
        Q(delivery_time__icontains=search_query) |
        Q(delivery_address__icontains=search_query) |
        Q(notes__icontains=search_query) | 
        Q(description__icontains=search_query)  |
        Q(recipent_name__icontains=search_query) |
        Q(phone__icontains=search_query) |
        Q(notes__icontains=search_query) 

        
        )
        context = {
            'couriers': couriers,
        }
        return render(request, 'Delivery/search_courier.html', context)
    else:
        return redirect('User:login')
def register_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            user = User.objects.get(username=request.POST.get('username'))
            login(request, user)

            #add user log
            return redirect('/')
            
        else:
            print(form.errors)
            context = {
                'error' : form.errors,
            }
            return render(request, 'User/register.html', context)
    else:
        return render(request, 'User/register.html')

def login_user(request):
    if request.user.is_authenticated:
        return redirect('User:index')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                #add user log
                return redirect('/')
        else:  
            return render(request, 'User/login.html')
    
#logout
def logout_user(request):
    
    #add user log
    logout(request)
    return redirect('User:login')

        