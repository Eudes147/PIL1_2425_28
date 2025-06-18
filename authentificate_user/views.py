from django.shortcuts import render,redirect 
from django.contrib.auth import authenticate,login 
from django.contrib.auth.views import LoginView
from .forms import ProfilForm, UtilisateurCreationForm
from .forms import ConnexionForm
from django.contrib.auth.decorators import login_required
from .models import Profil
from django.core.mail import send_mail
from django.contrib.auth import login


def inscription(request):
    if request.method == 'POST':
        form = UtilisateurCreationForm(request.POST)
        if form.is_valid():
            Utilisateur =form.save()
            login(request, Utilisateur)
            return redirect('profil')  
    else:
        form = UtilisateurCreationForm()
    return render(request, 'inscription.html', {'form': form})

def connexion(request):
    if request.method == 'POST':
        message = ""
        form = ConnexionForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('profil')
   
        else:
            message = "Nom d'utilisateur ou mot de passe incorrect.."
    else:
        form = ConnexionForm()
        message =""
    return render(request, 'connexion.html', {'form': form, 'message': message})


def accueil(request):
    return render(request, 'accueil.html')

class ConnexionView(LoginView):
    template_name = 'connexion.html'


@login_required(login_url='/connexion/')
def profil_view(request):
    profil,created = Profil.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = ProfilForm(request.POST, request.FILES, instance=profil)
        if form.is_valid():
            profil=form.save()
            profil.user = request.user
            profil.save()
            valeur = request.POST.get("conducteur")  # "true" ou "false"
            profil.conducteur = valeur == "true"
            profil.save()
            print(profil.conducteur)
            return redirect('accueil_secondaire',nameUser=profil.user.username)
    else:
        form = ProfilForm(instance=profil)
    return render(request, 'profil.html', {'form': form, 'profil': profil})