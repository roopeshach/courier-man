from django.shortcuts import render, redirect
from .models import Chat
from .forms import ChatForm
from django.contrib.auth.models import User
# Create your views here.

def chat(request, id):
    if request.method == 'POST':
        form = ChatForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/chat/' + str(id))
        else:
            print(form.errors)
    else:
        form = ChatForm()
    user = User.objects.get(id=id)
    chats = Chat.objects.all()
    #get users who started chat
    users = []
    for chat in chats:
        if chat.user not in users:
            users.append(chat.user)
    
    messages = Chat.objects.filter(user=user)
    context = {
        'form': form,
        'user': user,
        'users': users,
        'messages': messages,
    }
    return render(request, 'Chat/chat.html', context)


def users_chat(request):
    if request.method == 'POST':
        form = ChatForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/users-chat')
        else:
            print(form.errors)
    messages = Chat.objects.filter(user=request.user)
    context = {
        'messages': messages,
        'user': request.user,
    }
    return render(request, 'Chat/user-chat.html', context)
