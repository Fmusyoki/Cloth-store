from django.shortcuts import render,get_object_or_404,redirect
from .models import*
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.contrib import messages
from.models import User
from django.contrib.auth import authenticate, login as django_login
from django.contrib.auth import logout as django_logout
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.utils import timezone
from cart.forms import CartAddProductForm


# Create your views here.
# @login_required(login_url='/accounts/login/')
# def cat(request):
#     shirt = Product.objects.filter(trending=1)[:7]


def home(request):

        trending = Product.objects.filter(trending=1)[:7]
        arrivals = Product.objects.filter(new_arrivals=1)[:6]
        
        
        context ={
            'trending':trending,
            'arrivals':arrivals,
            }
            
        return render(request, "store/home.html", context)


def category(request, cat_id):
    category = Product.objects.filter(category=cat_id)
    categories = Category.objects.all()
    products = Product.objects.all()
    page = Paginator(products, 10)
    page_list = request.GET.get('page')
    page = page.get_page(page_list)
    context={
        'category':category,
        'categories':categories,
        'page':page,
    }
    
    return render(request, "store/category.html", context)
# @login_required
def shop(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    page = Paginator(products, 10)
    page_list = request.GET.get('page')
    page = page.get_page(page_list)



    context ={
        'categories':categories,
        'page':page,
        
    }
    return render(request, "store/shop.html", context)

def productsearch(request):
    categories = Category.objects.all()
    if request.method == "POST":
        searched = request.POST['searched']
        searches = Product.objects.filter(name__contains=searched)
    
    
    context ={
        'categories':categories,
        'searched':searched,
        'searches':searches 
    }
    
    return render(request, "store/search.html", context)

def productview(request,id):
    products = Product.objects.filter(id=id).first()
    # products = get_object_or_404(Product, id=id)
    related = Product.objects.filter(category=products.category).exclude(id=id)[:5]
    cart_product_form = CartAddProductForm()
    review = ProductReview.objects.filter(product=products)
    context={
        'p':products,
        'related':related,
        'cart_product_form':cart_product_form,
        'review':review,
    }
    
    
    return render(request, "store/detail.html",context)
 
def view_cart(request):
    return render(request, "store/cart.html")
        
        
            
def loginn(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            name = request.POST.get('username')
            passwd = request.POST.get('password')
            
            
            user = authenticate(request, username=name, password=passwd)
            
            if user is not None:
                django_login(request, user)
                return redirect('register')
            else:
                messages.warning(request, "user doesnt exist")
                return render(request, "store/home.html") 
                
                
        return render(request, "store/login.html") 
def register(request):
    msg = None
    success = False

    

    if request.method == "POST":
        Username = request.POST['username']
        Email = request.POST['Email']
        ConfirmPassword =request.POST['pass1']
        Password = request.POST['pass2']
        
        new_user = User(Username=Username, Email=Email, ConfirmPassword=ConfirmPassword, Password=Password)
        new_user.save()
    return render(request, "store/register.html")

def logout(request):
    django_logout(request)
    messages.success(request, "logout successfully")
    return redirect('login')

def review(request):
    if request.method == "POST":
        product = get_object_or_404(Product, id=id)
        review = request.POST['review']
        rating = request.POST['rating3']
        user = request.user
        Product_review=ProductReview(user=user, product=product, review=review, rate=rating)
        Product_review.save()
        return render(request, "store/detail.html")

def checkout(request):
    return render(request, "store/checkout.html")

def about(request):
    return render(request, "store/about.html")