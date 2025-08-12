from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from .forms import LoginForm, RegisterForm
from django.views import View
from .models import User, UserManager as create_user, ContactUs
from cart.models import Order










class UserLogin(View):
    def get(self, request):
        
        if request.user.is_authenticated:
            return redirect('home:main')
        

        
        
        
        form = LoginForm()
        
        return render(request, "account/Login.html", {'form':form})
    

    def post(self, request):
        if request.user.is_authenticated:
            return redirect('home:main')
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username = cd['phone'], password = cd['password'])
            
            if user is not None:
                login(request, user)
                next_page = request.GET.get('next')
                if next_page:
                    return redirect(next_page)
                return redirect('home:main')
            else:
                form.add_error('phone', 'شماره تلفن یا رمز خود را اشتباه وارد کرده اید ')
        


        return render(request, "account/Login.html", {'form':form})
    



class UserRegister(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('home:main')
        form = RegisterForm()
        return render(request, "account/Register.html", {'form':form})
    

    def post(self, request):
        if request.user.is_authenticated:
            return redirect('home:main')
        form = RegisterForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            if User.objects.filter(phone = cd['phone']).exists():
                form.add_error('phone', 'کاربری با این شماره وجود دارد ')
                
            else:
                if cd['password1'] == cd['password2']:
                    user = User.objects.create_user(phone=cd['phone'], password=cd['password1'], fullname=cd['fullname'])
                    login(request, user)
                    return redirect('home:main')
                else:
                    form.add_error('password1', 'رمز ها با یکدیگرد مطابقت ندارند')

                
        
        return render(request, "account/Register.html", {'form':form})





def contact_us(request):
    if request.method == 'POST':
        fullname = request.POST.get('fullname')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        body = request.POST.get('body')

        ContactUs.objects.create(
            
            fullname = fullname,
            email = email,
            subject = subject,
            body = body
            )
        return redirect('home:main')
    return render(request, 'account/contact_us.html')

    




def user_panel(request):
    if request.user.is_authenticated:
    
        order = Order.objects.filter(user = request.user)
        return render(request, 'account/user-profile.html', {'order':order})
    else:
        return redirect('account:login')






def logout_view(request):
    logout(request)
    return redirect('home:main')
