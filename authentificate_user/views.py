from django.shortcuts import render,redirect 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from .forms import ProfilForm, UtilisateurCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Profil
from authentificate_user.forms import Contact
from django.core.mail import send_mail

def inscription(request):
    if request.method == 'POST':
        form = UtilisateurCreationForm(request.POST)
        if form.is_valid():
            Utilisateur=form.save()
            return redirect('profil')  
    else:
        form = UtilisateurCreationForm()
    return render(request, 'inscription.html', {'form': form})

def connexion():
    return render(request, 'profil.html', {'form': form})


def accueil(request):
    return render(request, 'accueil.html')

class ConnexionView(LoginView):
    template_name = 'connexion.html'


def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method == 'POST':
        form = Contact(request.POST)
        if form.is_valid():
            send_mail(
                subject=f'Message from {form.cleaned_data["name"] or "anonyme"} via authentificate_user Contact form', 
                message = form.cleaned_data['message'],
                from_email=form.cleaned_data['email'],
                recipient_list=['ifricomotorage@gmail.com'],
            )
        return redirect('accueil')
    else:
        form = Contact()
    return render(request, 'contact.html', {'form':form})



@login_required
def profil_view(request):
    profil, created = Profil.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = ProfilForm(request.POST, request.FILES, instance=profil)
        if form.is_valid():
            profil=form.save()
            profil.user = request.user
            profil.save()
            return render(request,"matching/page_d'acceuil_secondaire.html",context={})
    else:
        form = ProfilForm(instance=profil)
    return render(request, 'profil.html', {'form': form, 'profil': profil})