from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 
from authentificate_user.models import Utilisateur
from .models import Profil

class UtilisateurCreationForm(UserCreationForm):
    # nom = forms.CharField(max_length=50)
    # prenom = forms.CharField(max_length=50)
    # email = forms.EmailField()
    # telephone = forms.CharField(max_length=15)
    # Role = forms.ChoiceField(choices=Utilisateur.role.choices)

    class Meta:
        model = Utilisateur
        fields = ('username','nom', 'prenom', 'email', 'telephone', 'Role', 'password1', 'password2')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'w-full border rounded px-3 py-2 mt-1 focus:outline-none focus:ring-2 focus:ring-green-500'}),
            'nom': forms.TextInput(attrs={'class': 'w-full border rounded px-3 py-2 mt-1 focus:outline-none focus:ring-2 focus:ring-green-500'}),
            'prenom': forms.TextInput(attrs={'class': 'w-full border rounded px-3 py-2 mt-1 focus:outline-none focus:ring-2 focus:ring-green-500'}),
            'email': forms.EmailInput(attrs={'class': 'w-full border rounded px-3 py-2 mt-1 focus:outline-none focus:ring-2 focus:ring-green-500'}),
            'telephone': forms.TextInput(attrs={'class': 'w-full border rounded px-3 py-2 mt-1 focus:outline-none focus:ring-2 focus:ring-green-500'}),
            'Role': forms.Select(attrs={'class': 'w-full border rounded px-3 py-2 mt-1 focus:outline-none focus:ring-2 focus:ring-green-500'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        style = 'w-full border rounded px-3 py-2 mt-1 focus:outline-none focus:ring-2 focus:ring-green-500'
        self.fields['password1'].widget.attrs.update({'class': style})
        self.fields['password2'].widget.attrs.update({'class': style})

class ProfilForm(forms.ModelForm):
    class Meta:
        model = Profil
        fields = ['photo', 'depart_lat', 'depart_lng', 'heure_depart', 'heure_arrivee', 'conducteur', 'marque', 'modele', 'places']

class Contact(forms.Form):
   name = forms.CharField(required=False, widget=forms.TextInput(attrs={
            'class': 'w-full border rounded px-3 py-2 mt-1 focus:outline-none focus:ring-2 focus:ring-green-500'
        }))
   email = forms.EmailField(widget=forms.EmailInput(attrs={
            'class': 'w-full border rounded px-3 py-2 mt-1 focus:outline-none focus:ring-2 focus:ring-green-500'
        }))
   message = forms.CharField(max_length=1000, widget=forms.TextInput(attrs={
            'class': 'w-full border rounded px-3 py-2 mt-1 focus:outline-none focus:ring-2 focus:ring-green-500'
        }))
