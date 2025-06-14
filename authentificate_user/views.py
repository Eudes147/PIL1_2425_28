from django.shortcuts import render,redirect 
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm
from django.contrib.auth.views import LoginView

def inscription(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('connexion')
    else:
            form = CustomUserCreationForm()
    return render(request, 'inscription.html', {'form':form})


def accueil(request):
    return render(request, 'accueil.html')

class ConnexionView(LoginView):
    template_name = 'connexion.html'


def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')