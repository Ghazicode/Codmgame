from django.shortcuts import render, redirect
from django.views import View
from product.models import Product
from .cart_module import Cart
from .models import Account, Order, OrderItem
from account.models import User




class CartDetailView(View): 
    def get(self, request):
        cart = Cart(request)
        
        
        return render(request, "cart/cart.html", {'cart':cart})



    
        



class CartAddView(View):
    def post(self, request, id):
        product = Product.objects.get(id = id)
        quantity = request.POST.get('quantity')
        cart = Cart(request)
        cart.add(product, quantity)
        return redirect('cart:cart_detail')
    


class CartDeleteView(View):
    def get(self, request, id):
        cart = Cart(request)
        cart.delete(id)
        return redirect('cart:cart_detail')
    










        
    
    
print()


class OrderCreationView(View):
    def get(self, request):
        cart = Cart(request)
        account = Account.objects.filter(user = request.user).last()
        order = Order.objects.create(user = request.user, total_price = int(cart.total()), account = account)
        for item in cart:
            OrderItem.objects.create(order = order, product = item['product'], quantity = item['quantity'], price = item['price'])

        

        cart.remove_cart()

        return redirect('cart:order_detail', order.id)







def account(request, pk):
    if request.method == 'POST':
        account = Account
        selected_value = request.POST.get('choice_value')
        email = request.POST.get('email')
        password = request.POST.get('password')
        gameid = request.POST.get('gameid')
        gamename = request.POST.get('gamename')

        
    
        account.objects.create(
            user = request.user,
            selected_value = selected_value,
            email = email, 
            password = password, 
            gameid = gameid, 
            gamename = gamename,
            )
    

    account = Account.objects.filter(user = request.user).last()
    orders = Order.objects.filter(id = pk,  user = request.user)
        
    orders.update(account = account)
    order = Order.objects.get(id = pk)
        

    return render(request, "cart/order_detail.html", {'order':order})









def pay(request):
    return render(request, 'cart/pay.html')