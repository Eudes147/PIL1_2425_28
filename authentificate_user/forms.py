from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 
from django.contrib.auth.models import AbstractUser
from .models import Profil

class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField (
        label = "Prénom",max_length=30, required = True,
    )
    last_name= forms.CharField(
        label="Nom",
        max_length=30, required = True,
    )

    Email=forms.EmailField(
        label="Adress Email",
        required = True,
    )
    Number = forms.CharField(
       label="Numéro de téléphone",
       max_length=15, required = True,
   )
    Role=forms.ChoiceField(
        label="Rôle",
        choices=[
            ('conducteur', 'Conducteur'),
            ('passager','Passager')
        ],
    )

    password1 = forms.CharField(
        label = "password",
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete':'new-password'}),
    )
    password2 =  forms.CharField(
        label = "password confirmation",
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete':'new-password'}),
    )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ("first_name","last_name","Email","Number","Role","password1","password2")


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
