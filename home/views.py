from django.shortcuts import render
from product.models import Product

# Create your views here.


def home(request):
    product_me = Product.objects.filter(status=True)[:8]
    return render(request, 'home/indexsh.html', context={'product_me': product_me})




