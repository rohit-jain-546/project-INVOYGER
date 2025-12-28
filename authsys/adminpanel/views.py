
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

from accounts.models import AdminUser
from .models import Product
from django.contrib import messages

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
    return render(request, 'adminpanel/adhome.html')
@login_required(login_url='/login/')
def adminpd(request):
    if not AdminUser.objects.filter(user=request.user).exists():
        return redirect('login')
    
    q=Product.objects.all()

    
    if request.GET.get('q'):
        q=q.filter(name__icontains=request.GET.get('q'))


    context={'products':q}
    return render(request, 'adminpanel/admin_pd.html', context)

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
    return render(request, 'adminpanel/update_product.html', context)
