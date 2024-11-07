from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Guide
from django.contrib.auth import login, authenticate, logout
from .forms import NewUserForm, GamePostForm
from django.contrib.auth.forms import AuthenticationForm

def home_page(request):
    categories = Category.objects.all()
    guides = Guide.objects.all()
    context = {
        'categories': categories,
        'guides': guides,
    }
    return render(request, "./home.html", context)

def description_page(request, pk):
    guide = get_object_or_404(Guide, pk=pk)
    context = {
        'guide': guide
    }
    return render(request, "./description.html", context)

def allguides_page(request):
    categories = Category.objects.all()
    guides = Guide.objects.all()
    context = {
        'categories': categories,
        'guides': guides,
    }
    return render(request, "./allguides.html", context)

def myguides_page(request):
    categories = Category.objects.all()
    guides = Guide.objects.all()
    context = {
        'categories': categories,
        'guides': guides,
    }
    return render(request, "./myguides.html", context)

def allgames_page(request):
    categories = Category.objects.all()
    guides = Guide.objects.all()
    context = {
        'categories': categories,
        'guides': guides,
    }
    return render(request, "./allgames.html", context)

def guides_by_category_page(request, slug):
    category = get_object_or_404(Category, slug=slug)
    guides = Guide.objects.filter(category=category)
    context = {
        'category': category,
        'guides': guides,
    }
    return render(request, "./guide_by_category.html", context)

def create_page(request):
    if request.method == 'POST':
        form = GamePostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect to a page after submission, e.g., home
    else:
        form = GamePostForm()
    return render(request, 'create.html', {'form': form})

def sign_up_page(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home_page')
    else:
        form = NewUserForm()
    context = {
        'form': form
    }
    return render(request, "./registration.html", context)

def login_page(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home_page')
    else:
        form = AuthenticationForm()

    context = {
        'form': form
    }
    return render(request, "./authorization.html", context)

def logout_action(request):
    logout(request)
    return redirect('home_page')