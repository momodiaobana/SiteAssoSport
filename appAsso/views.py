from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate, get_user_model
from django.contrib import messages
from .models import Products #import de la base product venant du modele 
from django.db.models import Sum
from django.contrib.auth.decorators import login_required
# Create your views here.


user = get_user_model()


###################### ACCUEIL ######################

def base(request):
    return render(request, "base.html")


def index(request):
    return render(request, "accueil.html")



###################### UTILISATEUR ######################

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
            return render(request, "userLogin.html", {'messages': messages})
    else:
        return render(request, "userLogin.html")



def signup(request):
    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        if user.objects.filter(username = username).exists() or user.objects.filter(email = email).exists():
            messages.error(request, 'Cet utilisateur existe déjà')
        else :
            utilisateur = user.objects.create_user(first_name = fname, last_name = lname, username = username, email = email, password = password)
            login(request, utilisateur)
            return redirect('accueil')

    return render(request, "signup.html")




###################### ACCUEIL ######################



def accueil(request):
    if request.user.is_authenticated:
        count_all_items = Products.objects.all().count()
        count_boxe_items = Products.objects.filter(cProduit = "boxe").count()
        count_basket_items = Products.objects.filter(cProduit = "basket").count()
        count_foot_items = Products.objects.filter(cProduit = "foot").count()
        ##### valeur totale du stok 
        items = Products.objects.all()
        valeur_totale_stock = sum(items.values_list('prix', flat=True))

        ##### prix moyen du stock
        if count_all_items > 0:
            prix_moyen = valeur_totale_stock / count_all_items
        else: 
            prix_moyen = 0
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
        return render(request, "accueil.html", context)
    return redirect('index')




########### PROFILE UTILISATEUR ###########


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
            request.user.first_name =  request.POST['fname']
            request.user.last_name = request.POST['lname']
            request.user.email = request.POST['email']
            mdp = request.POST['password']
            nouveauMdp = request.POST['newPassword']
            confirme = request.POST['confirmNewPassword']
            if mdp and not nouveauMdp and not confirme : 
                if request.user.check_password(mdp):
                    request.user.save()
                    messages.success(request, "Les informations ont été mis à jour avec succès!")
                    return redirect('updateProfil')
                else : 
                    messages.error(request, "Mot de passe incorrect")
                    return redirect('updateProfil')
            elif mdp and nouveauMdp and not confirme or (mdp and not nouveauMdp and confirme):
                messages.error(request, "Veuillez saisir les nouveaux mots de passe. Si vous ne souhaitez pas modifier votre mot de passe, ne remplissez pas votre nouveau mot de passe et la confirmation")
                return redirect('updateProfil')
            else:
                if not request.user.check_password(mdp):
                    messages.error(request, "Le mot de passe actuel est incorrect") 
                    return redirect('updateProfil')        
                else:
                    if nouveauMdp != confirme:
                        messages.error(request, "Le nouveau mot de passe et la confirmation ne correspondent pas")
                        return redirect('updateProfil')
                    elif nouveauMdp == mdp: 
                        messages.error(request, "Le nouveau mot de passe et l'ancien sont identiques")
                        return redirect('updateProfil')
                    else : 
                        request.user.set_password(nouveauMdp)
                        request.user.save()
                        messages.success(request, "Le mot de passe mis à jour avec succès!")
                        return redirect('profil')
        return render(request, 'updateProfil.html')



def userLogout(request):
    logout(request)
    return render(request, 'userLogout.html')


##### Gestion des produits ###########


def boxe(request):
    boxep = Products.objects.filter(cProduit = "boxe")
    context = {
        'boxep': boxep
        }

    #provisoire  
    if request.method == 'GET':
        search = request.GET.get('search')
        post = Products.objects.filter(cProduit="boxe").filter(nomProduit=search)
        context['post'] = post #merci à chatGPT pour cette ligne qui change tout 
    return render(request, 'boxe.html',context)
    


def foot(request):
    footp = Products.objects.filter(cProduit ="foot")
    context = {
        'footp':footp
    }
    #rechercher des elements à travers la barre de recherche 
    if request.method == 'GET':
        search = request.GET.get('search')
        post = Products.objects.all().filter(cProduit="foot").filter(nomProduit=search)
        context['post'] = post
            
    return render(request, 'foot.html', context)




def basket(request):
    basketp = Products.objects.filter(cProduit ="basket")
    context = {
        'basketp':basketp
    }

    #rechercher des elements à travers la barre de recherche 
    if request.method == 'GET':
        search = request.GET.get('search')
        post = Products.objects.all().filter(cProduit="basket").filter(nomProduit=search)
        context['post'] = post
    return render(request, 'basket.html', context)

    



def add(request): 
    if request.method == 'POST':
        nomProduit = request.POST['nomProduit']
        prix = request.POST['prix']
        cProduit = request.POST['cProduit']
        description = request.POST['description']
        newProduct = Products(nomProduit = nomProduit, prix=prix, cProduit = cProduit, description = description)
        newProduct.save()
    return render(request, "add.html", {})



def edit(request, id):
    items = Products.objects.get(id = id)
    label = {
        'nomProduit':'',
        'prix':'',
        'cProduit':'',
    }
        
    context = {
        'items' : items,
        'label':label
    }
    return render(request, 'edit.html', context)

    

#supprimer un element de la base
def deleteItem(request, id): 
    item = Products.objects.get(id = id)
    item.delete()
    return redirect('index')

