from django.shortcuts import redirect, render
from accounts.models import Customer
from adminpanel.models import Product
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login/')
def user_home(request):
    if not Customer.objects.filter(user=request.user).exists():
        return redirect('login')
    q=Product.objects.all()
    context={'products':q}

    return render(request, 'shop/home.html', context)
