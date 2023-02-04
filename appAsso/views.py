from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate, get_user_model
from django.contrib import messages
from .models import Products #import de la base product venant du modele 
from django.db.models import Sum
# Create your views here.





user = get_user_model()




def base(request):
    return render(request, "base.html")

def index(request):
    count_all_items = Products.objects.all().count()
    count_boxe_items = Products.objects.filter(cProduit = "boxe").count()
    count_basket_items = Products.objects.filter(cProduit = "basket").count()
    count_foot_items = Products.objects.filter(cProduit = "foot").count()
    ##### valeur totale du stok 
    items = Products.objects.all()
    valeur_totale_stock = sum(items.values_list('prix', flat=True))

    ##### prix moyen du stock
    prix_moyen = valeur_totale_stock / count_all_items

    ##### valeur du stock des articles de boxe 
    boxe_items = Products.objects.filter(cProduit = "boxe")
    valeur_stock_boxe = sum(boxe_items.values_list('prix', flat=True))
    ##### valeur du stock des articles de foot
    foot_items = Products.objects.filter(cProduit = "foot")
    valeur_stock_foot = sum(foot_items.values_list('prix', flat=True))
    ##### valeur du stock des articles de basket 
    basket_items = Products.objects.filter(cProduit = "basket")
    valeur_stock_basket = sum(basket_items.values_list('prix', flat=True))


    context = {'count_all_items': count_all_items, 
                'items':items,
                'count_boxe_items': count_boxe_items, 
                'count_basket_items': count_basket_items,
                'count_foot_items': count_foot_items,
                'valeur_totale_stock': float(valeur_totale_stock),
                'prix_moyen':float(prix_moyen), 
                'valeur_stock_boxe': float(valeur_stock_boxe), 
                'valeur_stock_foot': float(valeur_stock_foot), 
                'valeur_stock_basket': float(valeur_stock_basket),
                }
    return render(request, "acceuil.html", context)


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
    boxep = Products.objects.filter(cProduit = "boxe")
    context = {
        'boxep': boxep
        }

    #provisoire  
    if request.method == 'GET':
        search = request.GET.get('search')
        post = Products.objects.all().filter(cProduit="boxe").filter(nomProduit=search)
        return render(request, 'boxe.html', {'post': post})


    return render(request, 'boxe.html',context)


def foot(request):

    #rechercher des elements à travers la barre de recherche 
    if request.method == 'GET':
        search = request.GET.get('search')
        post = Products.objects.all().filter(cProduit="foot").filter(nomProduit=search)
        return render(request, 'foot.html', {'post': post})


    return render(request, 'foot.html')

def basket(request):
    #rechercher des elements à travers la barre de recherche 
    if request.method == 'GET':
        search = request.GET.get('search')
        post = Products.objects.all().filter(cProduit="basket").filter(nomProduit=search)
        return render(request, 'basket.html', {'post': post})
    return render(request, 'basket.html')


def adProduct(request):
    pass