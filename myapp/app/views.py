from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import SignUpForm, LoginForm
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
import os


# Create your views here.
def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'register.html', {'form': form})


def login_user(request):
    form = LoginForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(email=email, password=password, username=username)
            if user is not None:
                login(request, user)
                return redirect('books')
            else:
                form.add_error(None, "Неправильный email или пароль.")
    return render(request, 'login.html', {'form': form})


BOOK_FILE1 = os.path.join('static', 'books', "L.Tolstoi_tom_1.txt")
BOOK_FILE2 = os.path.join('static', 'books', "igra-prestolov-248812.txt")


@login_required
def logout_user(request):
    logout(request)
    return redirect('login')


def book_lev_tolskoi():
    with open(BOOK_FILE1, 'r') as file:
        return file.readlines()


def book_song_of_ice_and_fire():
    with open(BOOK_FILE2, 'r') as file:
        return file.readlines()


@login_required
def reed_book1(request):
    book_lines = book_lev_tolskoi()
    paginator = Paginator(book_lines, 30)
    page_number = request.GET.get('page')
    lines_to_display = paginator.get_page(page_number)

    return render(request, 'L.Tolstoi.html', {'context': lines_to_display, 'paginator': paginator})


@login_required
def reed_book2(request):
    book_lines = book_song_of_ice_and_fire()
    paginator = Paginator(book_lines, 30)
    page_number = request.GET.get('page', 1)
    lines_to_display = paginator.get_page(page_number)

    return render(request, 'game_of_the_thrones.html',
                  {'context': lines_to_display, 'paginator': paginator})


@login_required
def choosing_a_book(request):
    return render(request, "books.html")
