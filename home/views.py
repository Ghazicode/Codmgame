from django.shortcuts import render, get_object_or_404
from product.models import Category, Product





def home(request):
    category = Category.objects.all()
    return render(request, 'home/index.html', {'categorys':category})




def terms(request):
    return render(request, "home/terms.html",{})



def about(request):
    return render(request, "home/about.html", {})