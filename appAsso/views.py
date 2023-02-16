from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate, get_user_model
from django.contrib import messages
from .models import Products  # import de la base product venant du modele
from django.core.files.storage import FileSystemStorage


from django.contrib.auth.decorators import login_required
# Create your views here.


user = get_user_model()



###################### CONNEXION / DECONNEXION ######################


def userLogin(request):
    erreur = None
    if request.method == 'POST':
        username_or_email = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username_or_email, password=password) or \
            authenticate(email=username_or_email, password=password)
        if user:
            login(request, user)
            return redirect('accueil')
        else:

            erreur = 'Les informations d\'identification sont incorrectes.'
            # messages.error(request, 'Les informations d\'identification sont incorrectes')
            return render(request, "userLogin.html", {'erreur': erreur})
    else:
        return render(request, "userLogin.html")


def signup(request):
    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirme  = request.POST.get('cpassword')
        if user.objects.filter(username=username).exists() or user.objects.filter(email= email).exists():
            messages.error(request, 'Cet utilisateur existe déjà')
            return redirect('signup')
        else:
            if password == confirme : 
                utilisateur = user.objects.create_user(first_name=fname, last_name= lname, username = username, email = email, password = password)
                login(request, utilisateur)
                return redirect('accueil')
            else  : 
                messages.error(request, "Le mot de passe et la confirmation ne correspondent pas")
                return redirect ('signup')
    return render(request, 'signup.html')

###################### PAGES PRINCIPALES ######################


def base(request):
    return render(request, "base.html")


def index(request):
    return render(request, "accueil.html")


def accueil(request):

    count_all_items = Products.objects.all().count()
    count_boxe_items = Products.objects.filter(cProduit="boxe").count()
    count_basket_items = Products.objects.filter(cProduit="basket").count()
    count_foot_items = Products.objects.filter(cProduit="foot").count()
    # valeur totale du stok
    items = Products.objects.all()
    valeur_totale_stock = sum(items.values_list('prix', flat=True))

    # prix moyen du stock
    if count_all_items > 0:
        prix_moyen_ = valeur_totale_stock / count_all_items
        prix_moyen = round(prix_moyen_, 2)
    else:
        prix_moyen = 0
    # valeur du stock des articles de boxe
    boxe_items = Products.objects.filter(cProduit="boxe")
    valeur_stock_boxe = sum(boxe_items.values_list('prix', flat=True))
    # valeur du stock des articles de foot
    foot_items = Products.objects.filter(cProduit="foot")
    valeur_stock_foot = sum(foot_items.values_list('prix', flat=True))
    # valeur du stock des articles de basket
    basket_items = Products.objects.filter(cProduit="basket")
    valeur_stock_basket = sum(basket_items.values_list('prix', flat=True))

    context = {'count_all_items': count_all_items,
                'items': items,
                'count_boxe_items': count_boxe_items,
                'count_basket_items': count_basket_items,
                'count_foot_items': count_foot_items,
                'valeur_totale_stock': float(valeur_totale_stock),
                'prix_moyen': float(prix_moyen),
                'valeur_stock_boxe': float(valeur_stock_boxe),
                'valeur_stock_foot': float(valeur_stock_foot),
                'valeur_stock_basket': float(valeur_stock_basket),
            }
    return render(request, "accueil.html", context)

########### PROFIL UTILISATEUR ###########


def profil(request):
    if request.user.is_authenticated:
        user = request.user
        context = {
            'first_name': user.first_name if user.first_name else 'vide',
            'last_name': user.last_name if user.last_name else 'vide',
            'username': user.username if user.username else 'vide',
            'email': user.email if user.email else 'vide',
        }
        return render(request, 'profil.html', context)
    return redirect('index')


def updateProfil(request):
    if request.method == 'POST':
        username_or_email = request.POST['username']
        mdp = request.POST['password']
        nouveauMdp = request.POST['newpassword']
        confirme = request.POST['cpassword']
        user = authenticate(username=username_or_email, password=mdp) or \
            authenticate(email=username_or_email, password=mdp)
        if user : 
           if nouveauMdp != confirme:
                messages.error(request, "Le nouveau mot de passe et la confirmation ne correspondent pas")
                return redirect('updateProfil')
           elif nouveauMdp == mdp :
                messages.error(request, "Le nouveau mot de passe et l'ancien sont identiques")
                return redirect('updateProfil')
           else :
                user.set_password(nouveauMdp)
                user.save()
                messages.success(request, "Le mot de passe mis à jour avec succès!")
                return redirect('profil')
        else : 
            messages.error(request, "Les informations d'identification sont incorrects")
            return redirect('updateProfil')
    return render(request, 'updateProfil.html')


def userLogout(request):
    logout(request)
    return render(request, 'userLogout.html')


##### Gestion des produits ###########


def pages(request, categorie):
    produits = Products.objects.filter(cProduit=categorie)
    context = {'produits': produits}
    if request.method == 'GET':
        search = request.GET.get('search')
        post = Products.objects.filter(
            cProduit=categorie).filter(nomProduit=search)
        context['post'] = post

    return render(request, f'{categorie}.html', context)

def add(request):
    if request.method == 'POST':
        nomProduit = request.POST['nomProduit']
        prix = request.POST['prix']
        #gestion image 
        try:
            img = request.FILES['img']
            fs = FileSystemStorage()
            name = fs.save(img.name, img)
        except UnboundLocalError as e:
            print("erreur",e)
        except Exception as e: 
            print("erreur",e)

        cProduit = request.POST['cProduit']
        description = request.POST['description']
        newProduct = Products(nomProduit=nomProduit, prix=prix, cProduit= cProduit, img=img, description = description)
        newProduct.save()
    return render(request, "add.html", {})


def edit(request, id):
    items = Products.objects.get(id=id)
    if request.method == 'POST':
        nomProduit = request.POST['nomProduit']
        prix = request.POST['prix']
        cProduit = request.POST['cProduit']
        description = request.POST['description']
        items.nomProduit = nomProduit
        items.prix = prix
        items.cProduit = cProduit
        items.description = description
        items.save()
        return redirect('accueil')

    return render(request, 'edit.html', {'items': items})


# supprimer un element de la base
def deleteItem(request, id):
    item = Products.objects.get(id=id)
    item.delete()
    return redirect('accueil')

############## API REST ###############
from rest_framework.views import APIView
from appAsso.serializers import ProductSerializer
from rest_framework.response import Response

class ProductAPIView(APIView): 
    #initialisation d'un endpoint type get
    def get(self, *args, **kwargs): 
        product = Products.objects.all()
        serializer = ProductSerializer(product, many = True)
        return Response(serializer.data)
