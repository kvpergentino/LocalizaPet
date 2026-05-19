from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .models import Animal
from .forms import AnimalForm

def home(request):
    animais = Animal.objects.all().order_by('-id')
    return render(request, 'home.html', {'animais': animais})

# O 'login_required' redireciona automaticamente para a tela de login se o user não estiver logado
@login_required(login_url='login')
def cadastrar_pet(request):
    status_inicial = request.GET.get('status', 'perdido')
    
    if request.method == 'POST':
        form = AnimalForm(request.POST, request.FILES)
        if form.is_valid():
            # commit=False cria o objeto na memória mas não salva no banco ainda
            pet = form.save(commit=False)
            # Vinculamos o animal ao usuário que está enviando o formulário
            pet.usuario = request.user
            pet.save()
            messages.success(request, "Alerta publicado com sucesso!")
            return redirect('home')
    else:
        form = AnimalForm(initial={'status': status_inicial})
    
    return render(request, 'cadastrar.html', {'form': form})

# --- Funções de Autenticação ---

def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Conta criada com sucesso!")
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registro.html', {'form': form})

def logar(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, "Usuário ou senha inválidos.")
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def deslogar(request):
    logout(request)
    messages.success(request, "✅ Você foi deslogado com sucesso!")
    return redirect('home')

def detalhes_pet(request, pet_id):
    """Página de detalhes completos do pet"""
    pet = get_object_or_404(Pet, id=pet_id)
    return render(request, 'core/detalhes_pet.html', {'pet': pet})

#  Adicione esta função no final do arquivo views_pets.py

def detalhes_pet(request, pet_id):
    """
    Exibe os detalhes completos de um pet específico
    """
    from django.shortcuts import get_object_or_404
    
    pet = get_object_or_404(Animal, id=pet_id)
    
    # Verifica se o usuário atual é o dono do anúncio
    is_owner = False
    if request.user.is_authenticated:
        is_owner = (pet.usuario == request.user)
    
    # Processa a string de cores de volta para uma lista (se necessário)
    cores_list = []
    if pet.cores:
        cores_list = [cor.strip() for cor in pet.cores.split(',')]
    
    context = {
        'pet': pet,
        'is_owner': is_owner,
        'cores_list': cores_list,
    }
    
    return render(request, 'detalhes.html', context)