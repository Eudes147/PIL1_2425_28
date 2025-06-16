from django.utils import timezone
from django import forms
from .models import Offre,Demande
from datetime import date
from .models import max_length

class SomeForm(forms.ModelForm):
    class Meta:
        model = Offre
        fields = ["driver","departTime","nbPLacesDispo"]
        widgets = {
            "departPoint":{}
        }
    def cleanTask(self):
        deadline = self.cleaned_data["deadline"]
        if deadline < timezone.now().date():
            raise forms.ValidationError("Veuillez choisir une date future")
        return deadline