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


@login_required(login_url='login')
def cadastrar_pet(request):
    status_inicial = request.GET.get('status', 'perdido')

    if request.method == 'POST':
        form = AnimalForm(request.POST, request.FILES)
        if form.is_valid():
            pet = form.save(commit=False)
            pet.usuario = request.user
            pet.save()
            messages.success(request, "Alerta publicado com sucesso!")
            return redirect('home')
    else:
        form = AnimalForm(initial={'status': status_inicial})

    return render(request, 'cadastrar.html', {'form': form})


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
    messages.success(request, "Você foi deslogado com sucesso!")
    return redirect('home')


def detalhes_pet(request, pet_id):
    pet = get_object_or_404(Animal, id=pet_id)

    is_owner = request.user.is_authenticated and pet.usuario == request.user

    cores_list = [cor.strip() for cor in pet.cores.split(',')] if pet.cores else []

    context = {
        'pet': pet,
        'is_owner': is_owner,
        'cores_list': cores_list,
    }
    return render(request, 'detalhes.html', context)


@login_required(login_url='login')
def editar_pet(request, pet_id):
    pet = get_object_or_404(Animal, id=pet_id, usuario=request.user)

    if request.method == 'POST':
        form = AnimalForm(request.POST, request.FILES, instance=pet)
        if form.is_valid():
            form.save()
            messages.success(request, "Anúncio atualizado com sucesso!")
            return redirect('detalhes_pet', pet_id=pet.id)
    else:
        form = AnimalForm(instance=pet)

    return render(request, 'editar.html', {'form': form, 'pet': pet})


@login_required(login_url='login')
def deletar_pet(request, pet_id):
    pet = get_object_or_404(Animal, id=pet_id, usuario=request.user)

    if request.method == 'POST':
        pet.delete()
        messages.success(request, "Anúncio removido com sucesso!")
        return redirect('home')

    return render(request, 'deletar_anuncio.html', {'pet': pet})