from django.shortcuts import render
from .models import Product, Category




def category_detail(request, search):
    category = Category.objects.get(search=search)
    product = category.categorys.filter(status=True)
    return render(request, "product/product.html", {'products':product})





def product(request, search):
    product = Product.objects.get(search=search)
    popular = Product.objects.filter(popular = True)
    return render(request, 'product/product-detail.html', {'product':product, 'popular':popular})




def prices_list(request):
    pricelist = Product.objects.all()
    category = Category.objects.all()
    return render(request, 'product/prices-list.html', {'pricelist':pricelist, 'categorys':category})




def none(request):
    return render(request, "product/none.html", {})