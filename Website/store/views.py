# © 2020 Liran Smadja (First Real-World Project) ©
from django.shortcuts import render, redirect, HttpResponseRedirect, get_object_or_404
from django.contrib import messages
from .forms import UserRegisterForm, UpdateUserForm, UserLoginForm, UpdateShippingForm, storeRatingForm, UpdateProductForm, addProductForm, transactionForm, PromotedProductsForm, mainMessageForm, UpdateSellerForm, ContactSellerForm, ContactBuyerForm, contactSeller, addCoupon, contactSiteForm, productRatingForm, myShopListForm
from .models import *
from django.contrib.auth import login, logout
import datetime
from django.http import JsonResponse
import json
import random
import csv
from django.http import HttpResponse

from faker import Faker
from twilio.jwt.access_token import AccessToken
from twilio.jwt.access_token.grants import ChatGrant

fake = Faker()

def orderExcel(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="Orders.csv"'

    writer = csv.writer(response)
    writer.writerow(['date_ordered', 'complete', 'transaction_id', 'Buyer_id', 'pickup', 'id', 'total'])

    orders = Order.objects.all().values_list('date_ordered', 'complete', 'transaction_id', 'Buyer_id', 'pickup', 'id', 'total')
    for order in orders:
        writer.writerow(order)

    return response

def expansesExcel(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="Expanses.csv"'

    writer = csv.writer(response)
    writer.writerow(['expanse_name', 'startDate', 'endDate', 'amount'])

    expanses = Expenses.objects.all().values_list('expanse_name', 'startDate', 'endDate', 'amount')
    for expanse in expanses:
        writer.writerow(expanse)

    return response

def adminSettings(request): # count items in wishlist of logged in user
    advertise = Product.objects.all()
    form = mainMessageForm(request.POST or None, initial={'main_message': '', 'title': '' })
    PromotedProduct = PromotedProductsForm(request.POST, request.FILES, instance= PromotedProducts.objects.filter(unique_save=999).first())
    if request.method == 'POST':
        if form.is_valid():
            m = form.save(commit=False)
            m.save()
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('../')

        elif PromotedProduct.is_valid():
            m2 = PromotedProduct.save(commit=False)
            m2.save()
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('../')
    else:
        form = mainMessageForm(initial={'main_message': '', 'title': '' })
        PromotedProduct = PromotedProductsForm(request.POST, request.FILES, instance= PromotedProducts.objects.filter(unique_save=999).first() )

        context = {
            'form': form,
            'advertise_Products': advertise,
            'PromotedProduct': PromotedProduct

                 }
    return render(request, 'admin_settings.html', context)

def cart_scroll_view(request):
    if request.user.is_authenticated:
        buyer = Buyer.objects.filter(User_id=request.user.id).first()
        order, created = Order.objects.get_or_create(Buyer=buyer, complete=False)
        items = order.orderitem_set.all()
    else:
        # Create empty cart for error cart prevension
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}
    return items,order

def count_wishlist(request): # count items in wishlist of logged in user
    count = 0
    if request.user.is_authenticated:
        if request.user.is_superuser == True:
            return 0
        else:
            buyer = Buyer.objects.filter(User_id=request.user.id).first()
            items = buyer.wishlist_set.all()  # [ _set.all() ] lets you navigate backward between linked Table ForgienKeys (example: buyer exist in wishlist as ForgienKey ] ( tableName_set.all() )
            for count_items in items:
                if count_items.buyer_id == buyer.id:
                    count = count + 1
        return count
    else:
        return 0

def count_cart_items(request): # count items in wishlist of logged in user
    count = 0
    if request.user.is_authenticated:
        buyer  = Buyer.objects.filter(User_id=request.user.id).first()
        items = Order.objects.filter(Buyer_id=buyer, complete=False).first()
        return items.get_cart_items
    return 0


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

def searchPage(request):
    query = request.GET.get('LiranTheKing')
    products = Product.objects.filter(product_description__icontains=query)
    return render(request,'search.html', {
        'searched_items': products,
        'items': cart_scroll_view(request)[0],
        'order': cart_scroll_view(request)[1],
        'count': count_wishlist(request),
        'count_cart': count_cart_items(request),
        'main_message': mainMessage.objects.all().order_by('-id').first()
                                        } )

def categories(request,pk):
    product_info = Product.objects.filter(category=pk)
    product_count = Product.objects.filter(category=pk).count()

    #query = request.GET.get('LiranTheKing')
    #products = Product.objects.filter(product_description__icontains=query)
    #return render(request,'search.html', {'searched_items': products } )

    if request.method == 'POST':
        searchCheckBox = request.POST.get("searchCheckBox", None)
        if searchCheckBox in ["Electronics"]:
            products = Product.objects.filter(product_category__icontains='Electronics')
            return render(request, 'search.html', {'searched_items': products})

    context = {
        'product_info': product_info,
        'product_count': product_count,
        'product_category': pk,
        'count': count_wishlist(request),
        'count_cart': count_cart_items(request),
        'main_message': mainMessage.objects.all().order_by('-id').first()
          }
    return render(request,'category.html', context )

def sellerStoreRate(request,pk):
    seller_info = Seller.objects.filter(id=pk).first()
    form = storeRatingForm(request.POST or None, initial={'Seller': seller_info } )
    if request.method == 'POST':
        if form.is_valid():
            m = form.save(commit=False)
            m.save()
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('../../')
    else:
        form = storeRatingForm(initial={'Seller': seller_info } )
    return render(request,'seller_shop_rate.html', {'form': form, 'seller_info': seller_info, 'main_message': mainMessage.objects.all().order_by('-id').first() } )

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
    return render(request, 'user_messages.html', {'Messages_List_Buyer': Messages_List_Buyer, 'Messages_List_Seller': Messages_List_Seller, 'user_info': request.user , 'Seller': messageBySeller, 'Buyer': messageByBuyer, 'main_message': mainMessage.objects.all().order_by('-id').first() })

def adminMessages(request):
    Messages_List_Admin = contactSite.objects.all()
    return render(request, 'admin_messages.html', {'Messages_List_Admin': Messages_List_Admin } )

def sellerContact(request,pk):
    seller_info = Seller.objects.filter(id=pk).first()
    user_info = shippingAdd.objects.filter(User_id=seller_info.User_id).first()
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
    return render(request, "contact_seller.html", {'form': form, 'main_message': mainMessage.objects.all().order_by('-id').first(), 'seller_info': seller_info, 'user_info': user_info })

def contactUs(request):
    form = contactSiteForm(request.POST, request.FILES, initial={'body_text': '', 'title': '', 'first_name': '', 'last_name': '', 'email': ''})
    if request.method == 'POST':
        if form.is_valid():
            m = form.save(commit=False)
            m.save()
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('../')
    else:
        form = contactSiteForm()
    return render(request, "contact_site.html", {'form': form, 'main_message': mainMessage.objects.all().order_by('-id').first() })

def faq(request):
        if request.user.is_superuser == True:
            return render(request, 'faq_seller.html', {
                'main_message': mainMessage.objects.all().order_by('-id').first(),
                'count': count_wishlist(request),
                'count_cart': count_cart_items(request),
                'items': cart_scroll_view(request)[0],
                'order': cart_scroll_view(request)[1],
                                                      })
        else:
            return render(request,'faq.html', {
                'main_message': mainMessage.objects.all().order_by('-id').first(),
                'count': count_wishlist(request),
                'count_cart': count_cart_items(request),
                'items': cart_scroll_view(request)[0],
                'order': cart_scroll_view(request)[1],
                                              })

def coupons(request):
    coupons_list = Coupons.objects.all()
    return render(request,'admin_coupons.html', {'coupons': coupons_list, 'main_message': mainMessage.objects.all().order_by('-id').first() } )

def sellerAddCoupon(request):
    seller_info = Seller.objects.filter(User_id=request.user.id).first()
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
    return render(request, "seller_coupon_add.html", {'form': form, 'main_message': mainMessage.objects.all().order_by('-id').first(),'seller_info': seller_info,  })

def sellerCouponDelete (request,pk):
    item = get_object_or_404(Coupons, id=pk)
    item.delete()
    return redirect('../')

def buyerDeleteShop (request,pk):
    item = get_object_or_404(myShopList, id=pk)
    item.delete()
    return redirect('../../')


def sellerCoupons(request):
    seller_info = Seller.objects.filter(User_id=request.user.id).first()
    coupons_list = Coupons.objects.filter(Seller_id= seller_info.id )
    return render(request,'seller_coupons.html', {'coupons': coupons_list , 'Seller': seller_info, 'main_message': mainMessage.objects.all().order_by('-id').first() } )

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
    return render(request, "seller_product_review.html", {'form': form , 'product_id': pk, 'user_info': request.user, 'main_message': mainMessage.objects.all().order_by('-id').first() })

def adminMessageReview(request,pk):
    Messages_List_Admin = contactSite.objects.filter(id=pk).first()
    return render(request, 'admin_message_review.html', {'Messages_List_Admin': Messages_List_Admin } )

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

    return render(request, "user_message_review.html", {'form': form , 'user_info': request.user, 'details_seller': details_seller, 'details_buyer': details_buyer, 'main_message': mainMessage.objects.all().order_by('-id').first() } )

def sellerAddProduct(request):
    seller_info = Seller.objects.filter(User_id=current_user.id).first()
    form = addProductForm(request.POST or None, request.FILES, initial={'Seller': Seller.objects.filter(User_id=request.user.id).first()})
    if request.method == 'POST':
        if form.is_valid():
            m = form.save(commit=False)
            m.save()
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('../../my-products')
    else:
        form = addProductForm(initial={'Seller': Seller.objects.filter(User_id=request.user.id).first() })
    return render(request, "seller_product_add.html", {'form': form  , 'user_info': request.user, 'main_message': mainMessage.objects.all().order_by('-id').first(), 'seller_info': seller_info })

def wish_list(request):
    if request.user.is_authenticated:
        buyer= Buyer.objects.filter(User_id=request.user.id).first()
        items = buyer.wishlist_set.all() # [ _set.all() ] lets you navigate backward between linked Table ForgienKeys (example: buyer exist in wishlist as ForgienKey ] ( tableName_set.all() )
        seller = Seller.objects.all()
    else:
        items = [] # Create empty cart for error cart prevension

    context = {
        'items': items,
        'cart_items': cart_scroll_view(request)[0],
        'cart_order': cart_scroll_view(request)[1],
        'seller': seller,
        'count': count_wishlist(request),
        'count_cart': count_cart_items(request),
        'main_message': mainMessage.objects.all().order_by('-id').first()
              }
    return render(request, 'wishlist.html', context)


def SellerProducts(request): #admin panel product list
    data_product = {'product_list': Product.objects.all(),
                    'user_info': request.user,
                    'seller_info': Seller.objects.filter(User_id=request.user.id).first(),
                    'main_message': mainMessage.objects.all().order_by('-id').first()
                    }
    return render(request,'seller_products.html', data_product)

def cart(request):
	context = {
        'items':cart_scroll_view(request)[0],
        'order':cart_scroll_view(request)[1],
        'count_cart': count_cart_items(request),
        'count': count_wishlist(request),
        'main_message': mainMessage.objects.all().order_by('-id').first()
               }
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

    return JsonResponse('Item was added to cart', safe=False)


def updateWishlist(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    print('Action:', action)
    print('Product:', productId)

    buyer_info = Buyer.objects.filter(User_id=request.user.id).first()
    product = Product.objects.get(id=productId)
    items, created = wishlist.objects.get_or_create(buyer_id=buyer_info.id, product=product)

    if action == 'add':
        items.quantity = (items.quantity + 1)
    elif action == 'decrease':
        items.quantity = (items.quantity - 1)
    items.save()

    if action == 'remove':
        items.delete()

    if items.quantity <= 0:
        items.delete()

    return JsonResponse('Item was added to wishlist', safe=False)



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

def adminActivityLogs(request):
    user_info = User.objects.all()

    data = {'logs': lastLogin.objects.all(),
            'user_info': user_info
            }
    return render(request,'admin_activity_logs.html', data)

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
        return render(request, 'admin_user_add.html', {'form': form, 'user_info': request.user })

def reviewUser(request,pk):
    if not request.user.is_authenticated:
        return redirect('../../../')
    else:
        seller_info = Seller.objects.filter(User_id=pk).first()
        if request.method == 'POST':
            if not seller_info:
                storeForm = 0
            else:
                storeForm = UpdateSellerForm(request.POST, request.FILES, instance=seller_info , initial = { 'store_name': seller_info.store_name, 'store_category': seller_info.store_category, 'store_description': seller_info.store_description  })
            form = UpdateUserForm(request.POST, instance=User.objects.filter(id=pk).first())
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                messages.success(request, f'Account updated for {username}!')
                return redirect('../')

            elif storeForm.is_valid():
                storeForm = storeForm.save(commit=False)
                storeForm.save()
                return redirect('../')

        else:
            form = UpdateUserForm(instance=User.objects.filter(id=pk).first())
            if not seller_info:
                storeForm = 0
            else:
                storeForm = UpdateSellerForm(initial = { 'store_name': seller_info.store_name, 'store_category': seller_info.store_category, 'store_description': seller_info.store_description  })
        return render(request, 'admin_user_review.html', {
                                                    'form': form,
                                                    'user_info': request.user,
                                                    'storeForm': storeForm
                                                    })

def DeleteProduct (request,pk):
    item = get_object_or_404(Product, id=pk)
    item.delete()
    return redirect('../../../product-list')

def adminMessageDelete(request,pk):
    item = get_object_or_404(contactSite, id=pk)
    item.delete()
    return redirect('../../inbox')

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
    data_product = {'product_list': Product.objects.all(), 'user_info': request.user, 'main_message': mainMessage.objects.all().order_by('-id').first() }
    return render(request,'admin_product_list.html', data_product)

def userList(request): #admin panel user list
    data_user = {'user_list': User.objects.all() , 'user_info': request.user }
    return render(request,'admin_user_list.html', data_user)

def productDetails(request,pk):
    get_seller_from_product = Product.objects.filter(id=pk).first()
    seller_info = Seller.objects.filter(id=get_seller_from_product.Seller_id).first()
    get_comments = productRating.objects.filter(Product_id=pk)

# ---------------------------Add Views to Product Section ------------------------------------
    viewed = Product.objects.filter(id=pk).first() # update views of product by +1
    viewed.views= viewed.views+1# update views of product by +1
    viewed.save()# save update views of product by +1
# ---------------------------End Views to Product Section ------------------------------------

    if request.user.is_authenticated:
        buyer = Buyer.objects.filter(User_id=request.user.id).first()
        order, created = Order.objects.get_or_create(Buyer=buyer, complete=False)
        items = order.orderitem_set.all()
    else:
        # Create empty cart for error cart prevension
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}

    product = Product.objects.get(id=pk)
#---------------------------Rating Product Section ------------------------------------
    iterate_rating_column = productRating.objects.filter(Product_id=pk) #get all ratings from the same product
    item_rating_sum = 0 #initialize the counter for the rating sum of all the specific product
    count_items = len(iterate_rating_column) #get the number of ratings for the same product

    for item_rating in iterate_rating_column: # count the rating value of all ratings of thw specific item
        item_rating_sum = item_rating_sum + int(item_rating.rating)
    if (count_items == 0): #if there is not rating to the product then rating is -0-
        item_rating_avg = 0
    else:
        item_rating_avg = item_rating_sum//count_items #return the rating_amount/ ratings

    rating_to_product_table = product
    rating_to_product_table.rating = item_rating_avg
    rating_to_product_table.save()

    form = productRatingForm(request.POST or None, initial={'Product': product })
    if request.method == 'POST':
        if form.is_valid():
            m = form.save(commit=False)
            m.save()
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('../../')
    else:
        form = productRatingForm(initial={'Product': product } )

# ---------------------------End Rating Product Section ------------------------------------
    return render(request, 'product.html', {
        'items': items,
        'order': order,
        'product_info': product,
        'discount': product.discount,
        'priceWithDiscount': product.price*(1-(product.discount/100)),
        'user_details': request.user ,
        'seller_id': get_seller_from_product.Seller_id,
        'seller_info': seller_info,
        'form': form,
        'comments' : get_comments,
        'avg_rating': item_rating_avg,
        'main_message': mainMessage.objects.all().order_by('-id').first(),
        'count': count_wishlist(request),
        'count_cart': count_cart_items(request),
    } )

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
    return render(request, "admin_product_review.html", {'form': form , 'product_id': pk, 'user_info': request.user })


def error_404_view(request, exception):
    return render(request,'404.html',
                  {
                      'items': cart_scroll_view(request)[0],
                      'order': cart_scroll_view(request)[1],
                      'count': count_wishlist(request),
                      'count_cart': count_cart_items(request),
                      'main_message': mainMessage.objects.all().order_by('-id').first()

                  })

def adminPanel(request):
    if request.user.is_authenticated:
        order_count = 0
        for order in OrderItem.objects.all():
            order_count = order_count + order.get_total
        context = {
            'order_count': order_count,
            'count_products' : Product.objects.count(),
            'count_buyers': Buyer.objects.count(),
            'count_sellers': Seller.objects.count(),
            'user_info': request.user,
            'orders_info': Order.objects.all().order_by('-id')[:5],
            'countOnlineUsers': request.online_now.count(),
                  }
        return render(request,'admin_dashboard.html', context)
    else:
        return redirect ('../../../../../../')

def logoutPage(request):
    current_logout_log = lastLogin(time=datetime.datetime.now().strftime("%d/%m/%y %H:%M:%S"), User_id=request.user.id, ip=get_client_ip(request), logout = True)
    current_logout_log.save()
    return redirect('../logout')

def sellerSales(request):
    seller = Seller.objects.filter(User_id=request.user.id).first()
    orderitem = OrderItem.objects.filter(seller_id=seller.id)
    order = Order.objects.all()

    context = {
        'orderitem': orderitem,
        'order': order,
        'main_message': mainMessage.objects.all().order_by('-id').first()
            }
    return render(request, 'seller_sales.html', context )

def adminOrders(request):
    context = { }
    return render(request, 'admin_orders.html', context )

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
        return render(request, 'login.html', { 'form': form, 'main_message': mainMessage.objects.all().order_by('-id').first() })

def userPanel(request):
    if request.user.is_authenticated:
        current_user = request.user
        address = shippingAdd.objects.filter(User_id=current_user.id).first()
        user_info = User.objects.filter(id=current_user.id).first()
        seller_info  = Seller.objects.filter(User_id=current_user.id).first()
        data = {
            'user_info': user_info,
            'address' : address ,
            'seller_info': seller_info,
            'main_message': mainMessage.objects.all().order_by('-id').first()
                }
        return render(request, 'profile.html', data)
    else:
        data = {'user_info': '0'}
        return HttpResponseRedirect('/login')

def userUpdateInfo(request):
    userForm = UpdateUserForm(request.POST ,instance=request.user)
    storeForm = UpdateSellerForm(request.POST, request.FILES ,instance=Seller.objects.filter(User_id=request.user.id).first())
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
    return render(request, "update_info.html", {'form': form, 'form2': form2, 'main_message': mainMessage.objects.all().order_by('-id').first() })

def userUpdateShipping(request):
    current_user = request.user
    form = UpdateShippingForm(request.POST, instance=shippingAdd.objects.filter(User_id=current_user.id).first())
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
        form = UpdateShippingForm(instance=shippingAdd.objects.filter(User_id=current_user.id).first())
    return render(request, "update_shipping.html", {'form': form, 'main_message': mainMessage.objects.all().order_by('-id').first() })

def homePage(request):
    data_product = {'items': cart_scroll_view(request)[0],
                    'order': cart_scroll_view(request)[1],
                    'product_list': Product.objects.all(),
                    'countOnlineUsers': request.online_now.count(),
                    'count': count_wishlist(request),
                    'count_cart': count_cart_items(request),
                    'main_message': mainMessage.objects.all().order_by('-id').first(),
                    'promoted': PromotedProducts.objects.all().first()
                    }
    return render(request,'index.html', data_product )

def buyerShopList(request):
    shops_info = myShopList.objects.filter(User_id = request.user.id)
    context = {
        'shops_info': shops_info,
        'main_message': mainMessage.objects.all().order_by('-id').first()
    }
    return render(request, 'buyer_shop_list.html', context)

def orderCompleted(request,pk):
    if request.user.is_authenticated:
        buyer = Buyer.objects.filter(User_id=request.user.id).first()
        order, created = Order.objects.get_or_create(Buyer=buyer, complete=True, transaction_id=pk)
        items = order.orderitem_set.all()
    else:
        # Create empty cart for error cart prevension
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}

    shipping_info = shippingAdd.objects.filter(User_id=request.user.id).first()
    buyer_info = Buyer.objects.filter(User_id=request.user.id).first()
    get_transaction = Order.objects.filter(Buyer_id=buyer_info.id).first()  # get current transaction id of order
    confirmation_info = Order.objects.filter(transaction_id=  get_transaction.transaction_id).first()
    delivety_date = confirmation_info.date_ordered + datetime.timedelta(days=10)
    context = {
        'confirmation_info': confirmation_info,
        'order_id': pk,
        'order_details': order,
        'item_details': items,
        'shipping': shipping_info,
        'delivety_date': delivety_date,
        'count': count_wishlist(request),
        'count_cart': count_cart_items(request),
        'main_message': mainMessage.objects.all().order_by('-id').first()
    }
    return render(request, 'order_success.html', context)

def buyerOrderList(request):
    buyer_info = Buyer.objects.filter(User_id=request.user.id).first()
    order_info = Order.objects.filter(Buyer_id=buyer_info.id)
    context = {
             'buyer_info' : buyer_info,
             'order_info': order_info,
            'main_message': mainMessage.objects.all().order_by('-id').first()
              }
    return render(request, 'buyer_orders.html', context)

def checkout(request):
    if request.user.is_authenticated:
        if count_cart_items(request) == 0:
            return redirect('http://savebyclick.online')
        else:
            user_info = request.user
            buyer_info = Buyer.objects.filter(User_id=user_info.id).first()
            user_address = shippingAdd.objects.filter(User_id=user_info.id).first()
            get_transaction = Order.objects.filter(Buyer_id=buyer_info.id, complete=False).first() # get current transaction id of order
            form = transactionForm(request.POST or None, instance= Order.objects.filter(transaction_id=  get_transaction.transaction_id ).first() ,initial={'pickup': False, 'complete': True, 'Buyer': buyer_info.id, 'total': get_transaction.get_cart_total } )
            if request.method == 'POST':
                if form.is_valid():
                    m = form.save(commit=False)
                    m.save()
                    transec = Order.objects.filter(transaction_id=get_transaction.transaction_id).first()
                    transec.transaction_id = str(random.randint(10, 99)) + get_transaction.transaction_id + str(random.randint(10, 99))
                    transec.save()
                    success_url_redirect = '../../order/' + transec.transaction_id + '/success'
                    if 'next' in request.POST:
                        return redirect(request.POST.get('next'))
                    else:
                        return redirect(success_url_redirect)
            else:
                form = transactionForm(instance= Order.objects.filter(transaction_id=  get_transaction.transaction_id ).first(), initial={'pickup': False, 'complete': True, 'Buyer': buyer_info.id, 'total': get_transaction.get_cart_total } )

        context = {
            'user_info': user_info,
            'user_address': user_address,
            'order_info': cart_scroll_view(request)[1],
            'items_info': cart_scroll_view(request)[0],
            'form': form,
            'main_message': mainMessage.objects.all().order_by('-id').first(),
            'count': count_wishlist(request),
            'count_cart': count_cart_items(request),
        }
        return render(request, 'checkout.html', context)
    else:
        return redirect('http://savebyclick.online/cart')

def sellerShop(request,pk):
    iterate_rating_column = storeRating.objects.filter(Seller_id=pk)  # get all ratings from the same product
    item_rating_sum = 0  # initialize the counter for the rating sum of all the specific product
    count_items = len(iterate_rating_column)  # get the number of ratings for the same product

    for item_rating in iterate_rating_column:  # count the rating value of all ratings of thw specific item
        item_rating_sum = item_rating_sum + int(item_rating.rating)
    if (count_items == 0):  # if there is not rating to the product then rating is -0-
        item_rating_avg = 0
    else:
        item_rating_avg = item_rating_sum // count_items  # return the rating_amount/ ratings

    seller_info = Seller.objects.filter(id=pk).first()
    seller_products = Product.objects.filter(Seller_id=seller_info.id)
    my_shop_list = myShopList.objects.filter(store_id=seller_info.id).first()

    form = myShopListForm(request.POST or None, request.FILES, initial={'User': request.user.id, 'store_name':seller_info.store_name, 'image': seller_info.profile_image, 'store': seller_info.id })
    if request.method == 'POST':
        if form.is_valid():
            m = form.save(commit=False)
            m.save()
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('../../shop/'+ str(pk) )
    else:
        form = myShopListForm(initial={'User': request.user.id, 'store_name':seller_info.store_name, 'image': seller_info.profile_image, 'store': seller_info.id } )

    context = {
        'shop_details': seller_info,
        'seller_products': seller_products,
        'avg_shop_rate': item_rating_avg,
        'form': form,
        'my_shop_list': my_shop_list,
        'main_message': mainMessage.objects.all().order_by('-id').first()
              }
    return render(request, 'seller_shop.html', context)

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
        return render(request, 'register.html', {
            'form': form, 'main_message': mainMessage.objects.all().order_by('-id').first(),
            'items': cart_scroll_view(request)[0],
            'order': cart_scroll_view(request)[1],
            'count': count_wishlist(request),
            'count_cart': count_cart_items(request),
        })

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
    return render(request, "admin_product_add.html", {'form': form  , 'user_info': request.user, } )

# © 2020 Liran Smadja (First Real-World Project) ©