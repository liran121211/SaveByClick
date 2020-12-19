from django.shortcuts import render, redirect, HttpResponseRedirect, get_object_or_404
from django.contrib import messages
from .forms import UserRegisterForm, UpdateUserForm, UserLoginForm, UpdateShippingForm, UpdateProductForm, addProductForm, UpdateSellerForm, ContactSellerForm, ContactBuyerForm, contactSeller, addCoupon
from .models import *
from django.contrib.auth import login, logout
import datetime
from django.http import JsonResponse
import json

from faker import Faker
from twilio.jwt.access_token import AccessToken
from twilio.jwt.access_token.grants import ChatGrant

fake = Faker()

def token(request):
    identity = request.GET.get('identity', request.user.first_name)
    device_id = request.GET.get('device', 'default')  # unique device ID

    account_sid = 'AC7fccbb88242e2737fa5eddfee02a345b'
    api_key = 'SK7fcfaf886799640d8e8d2eb8bd0a0ce3'
    api_secret = 'A1WtIWMRG9fTPzTJ7LT0ZQEwWHNpoRtA'
    chat_service_sid = 'IS3e7465b31bb149f89ca4dd8fa629f233'

    token = AccessToken(account_sid, api_key, api_secret, identity=identity)

    # Create a unique endpoint ID for the device
    endpoint = "MyDjangoChatRoom:{0}:{1}".format(identity, device_id)

    if chat_service_sid:
        chat_grant = ChatGrant(endpoint_id=endpoint,
                               service_sid=chat_service_sid)
        token.add_grant(chat_grant)

    response = {
        'identity': identity,
        'token': token.to_jwt().decode('utf-8')
    }

    return JsonResponse(response)

def categoryMotors(request):
    x = { 'user': request.user.email }
    return render(request,'motors_category.html', x )

def all_rooms(request): #twilto chat
    rooms = Room.objects.all()
    return render(request, 'chat.html', {'rooms': rooms})


def room_detail(request, slug): #twilto chat
    room = Room.objects.get(slug=slug)
    return render(request, 'room_detail.html', {'room': room})

def userMessages(request):
    messageBySeller = Seller.objects.filter(User_id=request.user.id).first()
    messageByBuyer = Buyer.objects.filter(User_id=request.user.id).first()
    Messages_List_Seller = contactSeller.objects.all()
    Messages_List_Buyer = contactBuyer.objects.all()
    return render(request, 'user_messages.html', {'Messages_List_Buyer': Messages_List_Buyer, 'Messages_List_Seller': Messages_List_Seller, 'user_info': request.user , 'Seller': messageBySeller, 'Buyer': messageByBuyer })

def sellerContact(request,pk):
    form = ContactSellerForm(request.POST, initial={'User': request.user.id, 'body_text': '', 'title': '', 'first_name': '', 'last_name': '', 'email': '', 'receiver': pk })
    if request.method == 'POST':
        if form.is_valid():
            m = form.save(commit=False)
            m.save()
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('../../../profile')
    else:
        form = ContactSellerForm(initial={'User': request.user.id, 'body_text': '', 'title': '', 'first_name': '', 'last_name': '', 'email': '', 'receiver': pk })
    return render(request, "contact_seller.html", {'form': form })

def faq(request):
    return render(request,'faq.html')

def coupons(request):
    coupons_list = Coupons.objects.all()
    return render(request,'coupons.html', {'coupons': coupons_list } )

def sellerAddCoupon(request):
    form = addCoupon(request.POST or None, initial={'Seller': Seller.objects.filter(User_id=request.user.id).first()})
    if request.method == 'POST':
        if form.is_valid():
            m = form.save(commit=False)
            m.save()
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('../coupons')
    else:
        form = addCoupon(initial={'Seller': Seller.objects.filter(User_id=request.user.id).first() })
    return render(request, "seller_coupon_add.html", {'form': form  })

def sellerCouponDelete (request,pk):
    item = get_object_or_404(Coupons, id=pk)
    item.delete()
    return redirect('../')

def sellerCoupons(request):
    seller_info = Seller.objects.filter(User_id=request.user.id).first()
    coupons_list = Coupons.objects.filter(Seller_id= seller_info.id )
    return render(request,'seller_coupons.html', {'coupons': coupons_list , 'Seller': seller_info } )

def sellerReviewProduct(request,pk):
    form = UpdateProductForm(request.POST, request.FILES, instance= Product.objects.filter(id=pk).first() )
    if request.method == 'POST':
        if form.is_valid():
            m = form.save(commit=False)
            m.save()
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('../')
    else:
        form = UpdateProductForm(instance= Product.objects.filter(id=pk).first() )
    return render(request, "seller_product_review.html", {'form': form , 'product_id': pk, 'user_info': request.user })

def userMessageReview(request,pk):
    details_seller = contactSeller.objects.filter(id=pk).first()
    details_buyer = contactBuyer.objects.filter(id=pk).first()
    if request.user.is_superuser == True and request.user.is_staff == False:
        details_seller.read_or_not = False
        details_seller.save()
    elif request.user.is_superuser == False and request.user.is_staff == False:
        details_buyer.read_or_not = False
        details_buyer.save()
    form = ContactBuyerForm(request.POST, initial={'User': request.user.id, 'first_name': request.user.first_name, 'body_text': details_seller.body_text +'<p>----------------------------------------------------------------------------------------------------</p>' + 'Write Your Message Here' , 'title': 'Write Your Subject Here', 'last_name': request.user.last_name, 'email': request.user.email, 'receiver': details_seller.User_id })
    if request.method == 'POST':
        if form.is_valid():
            m = form.save(commit=False)
            m.save()
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('../')
    else:
        form = ContactBuyerForm(initial={'User': request.user.id, 'first_name': request.user.first_name, 'body_text': details_seller.body_text +'<p>----------------------------------------------------------------------------------------------------</p>' + 'Write Your Message Here', 'title': 'Write Your Subject Here', 'last_name': request.user.last_name, 'email': request.user.email, 'receiver': details_seller.User_id })

    return render(request, "user_message_review.html", {'form': form , 'user_info': request.user, 'details_seller': details_seller, 'details_buyer': details_buyer } )

def sellerAddProduct(request):
    form = addProductForm(request.POST or None, request.FILES, initial={'Seller': Seller.objects.filter(User_id=request.user.id).first()})
    if request.method == 'POST':
        if form.is_valid():
            m = form.save(commit=False)
            m.save()
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('../../product-list')
    else:
        form = addProductForm(initial={'Seller': Seller.objects.filter(User_id=request.user.id).first() })
    return render(request, "seller_product_add.html", {'form': form  , 'user_info': request.user })

def wish_list(request):
    wish =  wishlist.objects.filter(User_id=request.user.id)
    return render(request, 'wishlist.html', {'wish': wish } )

def SellerProducts(request): #admin panel product list
    data_product = {'product_list': Product.objects.all(),
                    'user_info': request.user,
                    'seller_info': Seller.objects.filter(User_id=request.user.id).first()
                    }
    return render(request,'seller_products.html', data_product)

def cart(request):
	if request.user.is_authenticated:
		buyer = Buyer.objects.filter(User_id=request.user.id).first()
		order, created = Order.objects.get_or_create(Buyer=buyer, complete=False)
		items = order.orderitem_set.all()
	else:
		#Create empty cart for error cart prevension
		items = []
		order = {'get_cart_total':0, 'get_cart_items':0}

	context = {'items':items, 'order':order }
	return render(request, 'cart.html', context)

def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    print('Action:', action)
    print('Product:', productId)

    buyer = Buyer.objects.filter(User_id=request.user.id).first()
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(Buyer=buyer, complete=False)
    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'decrease':
        orderItem.quantity = (orderItem.quantity - 1)
    orderItem.save()

    if action == 'remove':
        orderItem.delete()

    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse('Item was added', safe=False)

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

def addUser(request):
    if not request.user.is_authenticated:
        return redirect('../../../')
    else:
        if request.method == 'POST':
            form = UserRegisterForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                messages.success(request, f'Account created for {username}!')
                return redirect('../users')
        else:
            form = UserRegisterForm()
        return render(request, 'user_add.html', {'form': form, 'user_info': request.user })

def reviewUser(request,pk):
    if not request.user.is_authenticated:
        return redirect('../../../')
    else:
        if request.method == 'POST':
            form = UpdateUserForm(request.POST, instance=User.objects.filter(id=pk).first())
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                messages.success(request, f'Account updated for {username}!')
                return redirect('../')
        else:
            form = UpdateUserForm(instance=User.objects.filter(id=pk).first())
        return render(request, 'user_review.html', {'form': form, 'user_info': request.user })

def DeleteProduct (request,pk):
    item = get_object_or_404(Product, id=pk)
    item.delete()
    return redirect('../../../product-list')

def SellerDeleteProduct (request,pk):
    item = get_object_or_404(Product, id=pk)
    item.delete()
    return redirect('../../')

def sellerMessageDelete (request,pk):
    item = get_object_or_404(contactSeller, id=pk)
    item.delete()
    return redirect('../../')

def BuyerMessageDelete (request,pk):
    item = get_object_or_404(contactBuyer, id=pk)
    item.delete()
    return redirect('../../')

def DeleteUser (request,pk):
    item = get_object_or_404(User, id=pk)
    item.delete()
    return redirect('../../../users')

def productList(request): #admin panel product list
    data_product = {'product_list': Product.objects.all(), 'user_info': request.user }
    return render(request,'product_list.html', data_product)

def userList(request): #admin panel user list
    data_user = {'user_list': User.objects.all() , 'user_info': request.user }
    return render(request,'user_list.html', data_user)

def productDetails(request,pk):
    get_seller = Product.objects.filter(id=pk).first()
    viewed = Product.objects.filter(id=pk).first() # update views of product by +1
    viewed.views= viewed.views+1# update views of product by +1
    viewed.save()# save update views of product by +1
    if request.user.is_authenticated:
        buyer = Buyer.objects.filter(User_id=request.user.id).first()
        order, created = Order.objects.get_or_create(Buyer=buyer, complete=False)
        items = order.orderitem_set.all()
    else:
        # Create empty cart for error cart prevension
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}

    product = Product.objects.get(id = pk)
    return render(request, 'product.html', {'items': items, 'order': order, 'product_info': product, 'discount': product.discount, 'priceWithDiscount': product.price*(1-(product.discount/100)) , 'user_details': request.user , 'seller_id': get_seller.Seller_id})

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
    return render(request, "product_review.html", {'form': form , 'product_id': pk, 'user_info': request.user })


def error_404_view(request, exception):
    return render(request,'404.html')

def adminPanel(request):
    if request.user.is_authenticated:
        return render(request,'admin_dashboard.html', { 'user_info': request.user })
    else:
        return redirect ('../../../../../../')

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
    userForm = UpdateUserForm(request.POST ,instance=request.user)
    storeForm = UpdateSellerForm(request.POST, instance=Seller.objects.filter(User_id=request.user.id).first())
    if request.method == 'POST':
        if userForm.is_valid():
            m = userForm.save(commit=False)
            m.user = request.user
            m.save()
            
        elif storeForm.is_valid():
            m2 = storeForm.save(commit=False)
            m2.user = request.user
            m2.save()

            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('../profile')
    else:
        form = UpdateUserForm(instance=request.user)
        form2 = UpdateSellerForm(instance=Seller.objects.filter(User_id=request.user.id).first())
    return render(request, "update_info.html", {'form': form, 'form2': form2})

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
    if request.user.is_authenticated:
        buyer = Buyer.objects.filter(User_id=request.user.id).first()
        order, created = Order.objects.get_or_create(Buyer=buyer, complete=False)
        items = order.orderitem_set.all()
    else:
        # Create empty cart for error cart prevension
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}

    data_product = {'items': items,
                    'order': order,
                    'product_list': Product.objects.all(),
                    'countOnlineUsers': request.online_now.count()
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
        form = addProductForm(initial={'Seller': Seller.objects.filter(User_id=request.user.id).first() })
    return render(request, "product_add.html", {'form': form  , 'user_info': request.user } )