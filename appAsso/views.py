from django.shortcuts import render, HttpResponse
from django.contrib.auth import login, logout, authenticate, get_user_model
# Create your views here.




user = get_user_model()




def base(request):
    return render(request, "base.html")

def index(request):
    return render(request, "acceuil.html")


def signup(request):
    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        utilisateur = user.objects.create_user(first_name = fname, last_name = lname, username = username, email = email, password = password)
        login(request, utilisateur)
        return redirect('base')
    return render(request, "signup.html")


def login(request):
    if request.method == 'POST' :
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        if username : 
            utilisateur = authenticate(username = username, password = password)
        elif email: 
            utilisateur = authenticate(email = email, password = password)
        if utilisateur : 
            login(request, utilisateur)
            return redirect('base')
        else : 
           return HttpResponse("<script>alert('Identifiants incorrectes')</script>")
    return render(request, "login.html")