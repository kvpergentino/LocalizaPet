from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('cadastrar/', views.cadastrar_pet, name='cadastrar_pet'),
    path('registro/', views.registro, name='registro'),
    path('login/', views.logar, name='login'),
    path('logout/', views.deslogar, name='logout'),
    path('pet/<int:pet_id>/', views.detalhes_pet, name='detalhes_pet'),
    path('pet/<int:pet_id>/editar/', views.editar_pet, name='editar_pet'),
    path('pet/<int:pet_id>/deletar/', views.deletar_pet, name='deletar_pet'),
]