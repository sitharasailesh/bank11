from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.http import HttpResponse,JsonResponse




from django.shortcuts import render, redirect, get_object_or_404
# from demoapp.forms import AccountForm
# from demoapp.models import Branch


# Create your views here.
def home(request):
    return render(request,"base.html")

def register_form(request):
    return render(request,"registeration.html")
def page(request):
    return render(request,"page.html")
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        if not username or not password:
            messages.info(request, "Please fill all the fields")
            return render(request, "login.html")

        user = auth.authenticate(request, username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('page')
        else:
            messages.info(request, "Invalid credentials")
            return redirect('login')

    return render(request, "login.html")
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        cpassword = request.POST['password1']

        if username and password:
            if password == cpassword:
                if User.objects.filter(username=username).exists():
                    messages.info(request, "Username Already exists")
                else:
                    user = User.objects.create_user(username=username, password=password)
                    user.save()
                    return redirect('login')
            else:
                messages.info(request, "Passwords do not match")
        else:
            messages.info(request, "Username and password fields cannot be empty")

    return render(request, "register.html")
def logout(request):
    auth.logout(request)
    return redirect('/')
