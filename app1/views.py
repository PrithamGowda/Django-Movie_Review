from django.shortcuts import render,get_object_or_404,redirect
from .models import BookOrMovie, Genre, Review
from .forms import ReviewForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect


def home(request):
    query = request.GET.get('q')  # Get the search query
    genre_id = request.GET.get('genre')  # Get the selected genre ID

    # Start with all movies
    items = BookOrMovie.objects.all()

    # Apply genre filter if a genre is selected
    if genre_id:
        items = items.filter(genre_id=genre_id)

    # Apply search filter if a query is provided
    if query:
        items = items.filter(title__icontains=query)  # Case-insensitive partial match

    # Fetch all genres for the dropdown
    genres = Genre.objects.all()
    return render(request, 'index.html', {'items': items, 'genres': genres})

def item_detail(request, pk):
    item = get_object_or_404(BookOrMovie, pk=pk)
    reviews = item.reviews.all()
    form = ReviewForm(request.POST or None, initial={'item': item})
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('item_detail', pk=pk)
    return render(request,'index1.html', {'item': item, 'reviews': reviews, 'form': form})


def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'], 
                password=form.cleaned_data['password']
            )
            if user:
                login(request, user)
                return redirect('home')
            else:
                return render(request, 'login.html', {'form': form, 'error': 'Invalid credentials'})
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')


