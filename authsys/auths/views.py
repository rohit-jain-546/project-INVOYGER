from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.decorators import login_required
from auths.models import *
from django.contrib import messages



@login_required(login_url='/login/')
def user_home(request):
    if not Customer.objects.filter(user=request.user).exists():
        return redirect('login')

    return render(request, 'home.html')




@login_required(login_url='/login/')
def admin_home(request):
    if not AdminUser.objects.filter(user=request.user).exists():
        return redirect('login') 
    
    if request.method == "POST":
        product_name = request.POST.get("product_name")
        description = request.POST.get("description")
        price = request.POST.get("price")
        taxpercent = request.POST.get("taxpercent")
        stock = request.POST.get("stock")
        is_active = request.POST.get("is_active") == 'on'
        image = request.FILES.get("image")

        

        Product.objects.create(
            name=product_name,
            description=description,
            price=price,
            taxpercent=taxpercent,
            stock=stock,
            is_active=is_active,
            image=image
        )

        messages.success(request, "Product added successfully")
        return redirect('admin_home')
    return render(request, 'adhome.html')



def signup(request):
       if request.method == "POST":
            username = request.POST.get("username")
            email = request.POST.get("email")
            password = request.POST.get("password")
            role = request.POST.get("role")
            admin_code = request.POST.get("admin_code")

            if not all([username, email, password, role]):
               messages.error(request, "All fields are required")
               return redirect("signup")
            
            if User.objects.filter(username=username).exists():
               messages.error(request, "Username already exists")
               return redirect("signup")
            
            if role == "admin":
               if admin_code != "Rohit5460":
                    messages.error(request, "Invalid admin code")
                    return redirect("signup")

            user = User.objects.create_user(
                username=username,
                email=email,
                password=password
            )
            if role == "user":
               Customer.objects.create(user=user)
            elif role == "admin":
               AdminUser.objects.create(user=user)


            messages.success(request, "Account created successfully. Please login.")   
            return redirect('login')
       
       return render(request, 'signup.html')


def login_p(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        role = request.POST.get("role")

        user = authenticate(username=username, password=password)

        if user is None:
            messages.error(request, "Invalid username or password")
            return redirect("login")

        if role == "user":
            if Customer.objects.filter(user=user).exists():
                login(request, user)
                return redirect("user_home")
            else:
                messages.error(request, "You are not registered as a user")
                return redirect("login")

        if role == "admin":
            if AdminUser.objects.filter(user=user).exists():
                login(request, user)
                return redirect("admin_home")
            else:
                messages.error(request, "You are not registered as an admin")
                return redirect("login")

        messages.error(request, "Invalid login attempt")
        return redirect("login")

    return render(request, "login.html")

def logout_p(request):
    logout(request)
    messages.success(request, "You have been logged out")
    return redirect('login')

@login_required(login_url='/login/')
def adminpd(request):
    if not AdminUser.objects.filter(user=request.user).exists():
        return redirect('login')
    
    q=Product.objects.all()
    context={'products':q}
    return render(request, 'admin_pd.html', context)

def delete_product(request, product_id):
    if not AdminUser.objects.filter(user=request.user).exists():
        return redirect('login')
    
    try:
        product = Product.objects.get(id=product_id)
        product.delete()
        messages.success(request, "Product deleted successfully")
    except Product.DoesNotExist:
        messages.error(request, "Product does not exist")
    
    return redirect('adminpd')
# Create your views here.

def update_product(request, product_id):
    if not AdminUser.objects.filter(user=request.user).exists():
        return redirect('login')
    
    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        messages.error(request, "Product does not exist")
        return redirect('adminpd')

    if request.method == "POST":
        product.name = request.POST.get("product_name")
        product.description = request.POST.get("description")
        product.price = request.POST.get("price")
        product.taxpercent = request.POST.get("taxpercent")
        product.stock = request.POST.get("stock")
        product.is_active = request.POST.get("is_active") == 'on'
        
        if 'image' in request.FILES:
            product.image = request.FILES.get("image")

        product.save()
        messages.success(request, "Product updated successfully")
        return redirect('adminpd')

    context = {'product': product}
    return render(request, 'update_product.html', context)
