from django.contrib import admin

# Register your models here.
from .models import Offre,Demande

class OffreAdmin(admin.ModelAdmin):
    list_display = ('id', 'get_username', 'departTime', 'nbPlacesDispo', 'departlat', 'departlng') 
    def get_username(self, obj):
        return obj.driver.user.username

admin.site.register(Offre, OffreAdmin)

class DemandeAdmin(admin.ModelAdmin):
    list_display = ('id', 'get_username', 'departTime', 'departlat', 'departlng') 
    def get_username(self, obj):
        return obj.passenger.user.username

admin.site.register(Demande, DemandeAdmin)