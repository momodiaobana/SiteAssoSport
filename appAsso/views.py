from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate, get_user_model
from django.contrib import messages
from .models import Products
# Create your views here.





user = get_user_model()




def base(request):
    return render(request, "base.html")

def index(request):
    return render(request, "acceuil.html")


def signup(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            return redirect('userLogin')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        utilisateur = user.objects.create_user(first_name = fname, last_name = lname, username = username, email = email, password = password)
        login(request, utilisateur)
        return redirect('index')
    return render(request, "signup.html")



def userLogin(request):
    if request.method == 'POST':
        username_or_email = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username_or_email, password=password) or \
               authenticate(email=username_or_email, password=password)
        if user:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Les informations d\'identification sont incorrectes')
    return render(request, "userLogin.html")




def boxe(request):
    boxep = Products.objects.filter(cProduit = "BOXE")
    return render(request, 'boxe.html',{'boxep': boxep})


def foot(request):
    return render(request, 'foot.html')

def basket(request):
    return render(request, 'basket.html')


def adProduct(request):
    pass