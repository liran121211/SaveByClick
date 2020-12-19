from django.shortcuts import render, redirect, HttpResponseRedirect, get_object_or_404
from django.contrib import messages
from .forms import UserRegisterForm, UpdateUserForm, UserLoginForm, UpdateShippingForm, UpdateProductForm, addProductForm
from .models import *
from django.contrib.auth import login, logout
import datetime


PRIVATE_IPS_PREFIX = ('10.', '172.', '192.', )
def get_client_ip(request):
    remote_address = request.META.get('REMOTE_ADDR')
    ip = remote_address
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        proxies = x_forwarded_for.split(',')
        while (len(proxies) > 0 and
                proxies[0].startswith(PRIVATE_IPS_PREFIX)):
            proxies.pop(0)
        if len(proxies) > 0:
            ip = proxies[0]

    return ip

def activity_logs(request):
    current_user = request.user
    data = {'logs': lastLogin.objects.filter(User_id = current_user.id), 'user_info': User.objects.filter(id=current_user.id).first()}
    return render(request,'activity_logs.html', data)

def DeleteProduct (request,pk):
    item = get_object_or_404(Product, id=pk)
    item.delete()
    return redirect('../../../product-list')

def productList(request): #admin panel product list
    data_product = {'product_list': Product.objects.all() }
    return render(request,'product_list.html', data_product)

def userList(request): #admin panel user list
    data_user = {'user_list': User.objects.all() }
    return render(request,'user_list.html', data_user)

def productDetails(request,pk):
    product = Product.objects.get(id = pk)
    return render(request, 'product.html', {'product_info': product, 'discount': product.discount, 'priceWithDiscount': product.price*(1-(product.discount/100)) })

def reviewProduct(request,pk):
    form = UpdateProductForm(request.POST, request.FILES, instance=Product.objects.filter(id=pk).first())
    if request.method == 'POST':
        if form.is_valid():
            m = form.save(commit=False)
            m.save()
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('../../../product-list')
    else:
        form = UpdateProductForm(instance=Product.objects.filter(id=pk).first())
    return render(request, "product_review.html", {'form': form , 'product_id': pk})


def error_404_view(request, exception):
    return render(request,'404.html')

def adminPanel(request):
    return render(request,'admin_dashboard.html')

def logoutPage(request):
    current_logout_log = lastLogin(time=datetime.datetime.now().strftime("%d/%m/%y %H:%M:%S"), User_id=request.user.id, ip=get_client_ip(request), logout = True)
    current_logout_log.save()
    return redirect('../logout')

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method == 'POST':
            form = UserLoginForm(data=request.POST)
            if form.is_valid():
                # log the user in
                user = form.get_user()
                login(request, user)
                if 'next' in request.POST:
                    return redirect(request.POST.get('next'))
                else:
                   current_login_log = lastLogin(time= datetime.datetime.now().strftime("%d/%m/%y %H:%M:%S") ,User_id = request.user.id, ip = get_client_ip(request), logout = False)
                   current_login_log.save()
                   if (request.user.is_superuser == True and request.user.is_staff == True):
                       return redirect('/admin-panel')
                return redirect('/')
        else:
            form = UserLoginForm()
        return render(request, 'login.html', { 'form': form })

def userPanel(request):
    if request.user.is_authenticated:
        current_user = request.user
        address = shippingAdd.objects.filter(shipping_id=current_user.id).first()
        data = {'user_info': User.objects.filter(id=current_user.id).first(), 'address' : address}
        return render(request, 'profile.html', data)
    else:
        data = {'user_info': '0'}
        return HttpResponseRedirect('/login')

def userUpdateInfo(request):
    form = UpdateUserForm(request.POST, instance=request.user)
    if request.method == 'POST':
        if form.is_valid():
            m = form.save(commit=False)
            m.user = request.user
            m.save()
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('../login')
    else:
        form = UpdateUserForm(instance=request.user)
    return render(request, "update_info.html", {'form': form})

def userUpdateShipping(request):
    current_user = request.user
    form = UpdateShippingForm(request.POST, instance=shippingAdd.objects.filter(shipping_id=current_user.id).first())
    if request.method == 'POST':
        if form.is_valid():
            m = form.save(commit=False)
            m.user = request.user
            m.save()
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('../profile')
    else:
        form = UpdateShippingForm(instance=shippingAdd.objects.filter(shipping_id=current_user.id).first())
    return render(request, "update_shipping.html", {'form': form })

def homePage(request):
    data_product = { 'product_list': Product.objects.all()
                     }
    return render(request,'index.html', data_product )


def Checkout(request):
    context = {
        'key': '0'
    }
    return render(request, 'checkout.html', context)

def RegisterPage(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method == 'POST':
            form = UserRegisterForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                messages.success(request, f'Account created for {username}!')
                return redirect('/login')
        else:
            form = UserRegisterForm()
        return render(request, 'register.html', {'form': form})

def addProduct(request):
    form = addProductForm(request.POST or None, request.FILES, initial={'Seller': Seller.objects.filter(User_id=request.user.id).first() })
    if request.method == 'POST':
        if form.is_valid():
            m = form.save(commit=False)
            m.save()
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('../../product-list')
    else:
        form = addProductForm(initial={'Seller': '1' })
    return render(request, "product_add.html", {'form': form  } )