from django.shortcuts import render,redirect
# Create your views here.
from .forms import OrderForm,CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .models import *


@login_required(login_url='login')
def home(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()

    total_orders = orders.count()
    total_delivered = orders.filter(status = 'Delivered').count()
    total_pending = orders.filter(status = 'Pending').count()

    context = {
        'orders':orders,
        'customers':customers,
        'total_orders':total_orders,
        'total_delivered':total_delivered,
        'total_pending':total_pending
        }

    return render(request,'accounts/home.html',context)


@login_required(login_url='login')
def products(request):
    products = Product.objects.all()
    return render(request,'accounts/products.html',{'products':products})

@login_required(login_url='login')
def customer(request,pk):
    customer = Customer.objects.get(id=pk)
    orders = customer.order_set.all()
    orders_count = orders.count()
    context = {'customer':customer,'orders':orders,'orders_count':orders_count}
    return render(request,'accounts/customer.html',context)       

def createOrder(request):

    form = OrderForm()

    if request.method == 'POST':
        print(request.POST)
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form':form};
    return render(request,'accounts/order_form.html',context)  


def updateOrder(request,key):
    order = Order.objects.get(id=key)
    form = OrderForm(instance=order)

    if request.method == 'POST':
        form = OrderForm(request.POST,instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form':form}
    return render(request,'accounts/order_form.html',context)  


def deleteOrder(request,key):
    order = Order.objects.get(id=key)

    if request.method == 'POST':
        order.delete()
        return redirect('/')

    context={'item':order}
    return render(request,'accounts/delete.html',context)  


def registerPage(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('login')    
    
    context={'form':form}
    return render(request,'accounts/register.html',context)

def loginPage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request,username = username,password = password)

        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.info(request,'Username or Password incorrect')    
    context={}
    return render(request,'accounts/login.html')

def logoutUser(request):
    logout(request)
    return redirect('login')    
