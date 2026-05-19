from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('cadastrar/', views.cadastrar_pet, name='cadastrar_pet'),
    path('registro/', views.registro, name='registro'), # Nova
    path('login/', views.logar, name='login'),          # Nova
    path('logout/', views.deslogar, name='logout'),    # Nova
    path('pet/<int:pet_id>/', views.detalhes_pet, name='detalhes_pet'),
]