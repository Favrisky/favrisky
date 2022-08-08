from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Feature
# Create your views here.
def index(request):
    return render(request, 'index.html')
def about(request):
    return render(request, 'about.html')
def blog(request):
    return render(request, 'blog.html')
def contact(request):
    return render(request, 'contact.html')
def services(request):
    return render(request, 'services.html')
def testimonial(request):
    return render(request, 'testimonial.html')
def logout(request):
    auth.logout(request)
    return redirect('/')
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(usernsme=username, password=password)

        if user is None:
            auth.login(request, user)
            return redirect('/')

        else:
            messages.info(request, 'Credentials Incorrect')
            return redirect('login')
    else:
        return render(request, 'login.html')
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email in Use')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username already exists')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save();
                return redirect('/login')
        else:
            messages.info(request, 'Password Not The same')
            return redirect('register')
    return render(request, 'register.html')



    