from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
from .models import Buyer

def userPanel(request):
    data = {'key': Buyer.objects.filter(id =1)}
    return render(request, 'user.html', data)

def homePage(request):
    context = {
        'key': '0'
    }
    return render(request,'home.html', context)

def Products(request):
    context = {
        'key': '0'
    }
    return render(request, 'product.html', context)

def Checkout(request):
    context = {
        'key': '0'
    }
    return render(request, 'checkout.html', context)

def RegisterPage(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('http://savebyclick.online/admin/login/?next=/admin/')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})
