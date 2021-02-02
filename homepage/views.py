from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import *
from .filters import ProductFilter
from django.contrib.auth.models import User, auth
from django.contrib import messages
import json
import datetime
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string
import random

# Create your views here.


def home(request):
    return render(request, 'index.html')


def store(request):
    products = Product.objects.all()
    myfilter = ProductFilter(request.GET, queryset=products)
    products = myfilter.qs
    return render(request, 'store.html', {'products': products, 'myfilter': myfilter})


def accounts(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        return render(request, 'accounts.html')


def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer  # if the user is logged in , we take the user as a customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        context = {'items': items, 'order': order}
    else:
        context = {}
        pass
    return render(request, 'cart.html', context)


def update_item(request):
    if request.user.is_authenticated:
        data = json.loads(request.body)  # parsing the data
        productid = data['product-id']
        action = data['action']
        price = data['price']
        customer = request.user.customer
        product = Product.objects.get(id=productid)  # get the product that we need to add
        try:
            if float(price) == product.price1:
                asset = product.price1
            elif float(price) == product.price2:
                asset = product.price2
            elif float(price) == product.price3:
                asset = product.price3

        except ValueError:
            if price == 'price1':
                asset = product.price1
            elif price == 'price2':
                asset = product.price2
            elif price == 'price3':
                asset = product.price3

        print(asset)

        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        if OrderItem.objects.filter(order=order, product=product, price=asset).exists():
            orderItem = OrderItem.objects.get(order=order, product=product, price=asset)
        else:
            orderItem = OrderItem.objects.create(order=order, product=product, price=asset)

        if action == 'add':
            orderItem.quantity = orderItem.quantity + 1
        elif action == 'remove':
            orderItem.quantity = orderItem.quantity - 1
        orderItem.save()
        if orderItem.quantity <=0:
            orderItem.delete()
    else:
        pass
    return JsonResponse('item was added', safe=False)


def processOrder(request):
    transaction_id = datetime.datetime.now().timestamp()
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        if request.method == 'POST':
            customer.name = request.POST['customer_name']
            customer.email = request.POST['email']
            customer.contact_no = request.POST['contact_no']
            customer.save()
            total = request.POST['cart_total']
            items_no = order.get_cart_items
            address=request.POST['store_address']
            if float(request.POST['cart_total']) == order.get_cart_total:
                order.order_total = order.get_cart_total
                order.complete = True
                for item in items:
                    item.ordered = True
                    item.customer = request.user.customer
                    item.date_added = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
                    item.save()
                order.transaction_id = transaction_id
                order.save()
                shipping = Shipping.objects.create(
                    customer=customer,
                    order=order,
                    store_address=request.POST['store_address']
                )
                template = render_to_string('order_success_mail.html',{'name':customer.name,'address':address,'transaction_id':transaction_id ,'total':total,'items_no':items_no,'items':items})
                email_send = EmailMessage(
                    'Happy Shopping!!',
                    template,
                    settings.EMAIL_HOST_USER,
                    [customer.email], 
                ) 
                email_send.fail_silently = False
                email_send.send()
            else:
                print("abe apne baap se panga le raha hai ,cheating krta hai sala")
    context = {'name': customer.name, 'contact_no':customer.contact_no, 'email':customer.email,'items': items_no,'total':total,'transaction_id':transaction_id, 'address':address}
    return render(request, 'order_success.html',context)


def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer  # if the user is logged in , we take the user as a customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        context = {'items': items, 'order': order}
    else:
        context = {}
        pass
    return render(request, 'checkout.html',context)


def customer(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        item = customer.orderitem_set.filter(ordered=True)
        total_items = item.count()
        delivered = customer.orderitem_set.filter(status='Delivered', ordered=True).count()
        out_for_delivery = customer.orderitem_set.filter(status='Out for delivery', ordered=True).count()
        context = {'items':item,'total_items':total_items,'delivered':delivered, 'out_for_delivery':out_for_delivery}
    else:
        return redirect('accounts')
    return render(request,'customer.html', context)


def deleteUser(request):
    if request.user.is_authenticated:
        username = request.user
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
           username.delete()
           messages.success(request,'Account Deleted Successfully')
           return redirect('accounts')
        else:
            messages.error(request, 'Deletion Unsuccessfull')
            return redirect('customer')
    

def updateEmail(request):
    if request.user.is_authenticated:
        username = request.user
        password = request.POST['password']
        email = request.POST['email']
        user = auth.authenticate(username=username, password=password)
        print(username.email)
        print(email)
        if username.email != email:
            if user is not None:
                username.email = email
                username.save()
                messages.success(request,'Email Updated Sucessfully')
                return redirect('customer')
            else:
                messages.error(request, 'Incorrect Password')
                return redirect('customer')
        else:
            messages.error(request,'Email already registered')
            return redirect('customer')


def deleteItem(request,pk):
    item = OrderItem.objects.get(id=pk)
    item.delete()
    return redirect('customer')


def feedback(request,pk):
    item = OrderItem.objects.get(id=pk)
    if request.method == 'POST':
        item.feedback = request.POST['feedback']
        item.save()
    return render(request,'feedback.html',{'item':item})

def contact(request):
    firstname = request.POST['firstname']
    lastname = request.POST['lastname']
    email = request.POST['email']
    phoneno = request.POST['phoneno']

    cntct1 = ContactForm(
        FirstName=firstname,
        LastName=lastname,
        Email=email,
        PhoneNo=phoneno
    )
    cntct1.save()
    template = render_to_string('email_message.html',{'name':firstname})
    email_send = EmailMessage(
            'Thank For Contacting us',
            template,
            settings.EMAIL_HOST_USER,
            [email], 
        ) 
    email_send.fail_silently = False
    email_send.send()
    return redirect('/')


def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        fname = request.POST['firstname']
        lname = request.POST['lastname']
        uname = request.POST['username']
        mail = request.POST['email']
        pswd1 = request.POST['password1']
        pswd2 = request.POST['password2']

        if pswd1 == pswd2:
            if User.objects.filter(username=uname).exists():
                messages.error(request, 'username already taken')
                return redirect('accounts')
            elif User.objects.filter(email=mail).exists():
                messages.error(request, 'email already registered')
                return redirect('accounts')
            else:
                user = User.objects.create_user(username=uname, email=mail, first_name=fname, last_name=lname,
                                                password=pswd1)
                user.save()
                messages.success(request, 'Registered successfully')
                return redirect('accounts')

        else:
            messages.error(request, 'password does not match')
            return redirect('accounts')


def login_user(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        uname = request.POST['lgnusername']
        pswd = request.POST['password']

        user = auth.authenticate(username=uname, password=pswd)

        if user is not None:
            auth.login(request, user)
            customer = Customer.objects.get_or_create(
                user=request.user,
                name=request.user.first_name,
                email=request.user.email
            )
            return redirect('/')
        else:
            messages.error(request, 'INVALID CREDENTIALS')
            return redirect('accounts')


def verifyemail(request):
    if request.method == 'POST':
        pass
    else:
        otp = random.randint(1000,9999)
        print('random no : ',otp)
        template = render_to_string('email_message.html',{'name':request.user.first_name,'otp':otp})
        email = EmailMessage(
            'Email Verififcation',
            template,
            settings.EMAIL_HOST_USER,
            [request.user.email], 
        ) 
        email.fail_silently = False
        email.send()
        return None
        

def logout(request):
    auth.logout(request)
    return redirect('accounts')