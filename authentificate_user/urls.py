from django.contrib import admin
from django.urls import path
from authentificate_user import views
from .views import accueil, ConnexionView ,about, contact
from django.contrib.auth import views as auth_views

urlpatterns = [
    
    path('', views.inscription, name='inscription'),
    path('accueil/', accueil, name='accueil'),
    path('connexion/', ConnexionView.as_view(), name='connexion'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='password_reset.html'), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),
]