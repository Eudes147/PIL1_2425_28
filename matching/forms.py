from django.utils import timezone
from django import forms
from .models import Offre,Demande
from datetime import date

class SomeForm(forms.ModelForm):
    class Meta:
        model = Offre
        fields = ["driver","departTime","nbPLacesDispo"]
        widgets = {
            'departPoint': {
                'departTime': forms.TextInput(attrs={"disabled":True,"title":"Point de départ"}),
                'endTime': forms.TextInput(attrs={"disabled":True,"title":"Point de départ"})
            }
        }
        labels = {
            "departTime":"",
            "endTime":""
        }