"""
URL configuration for myapp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app.views import register_user, login_user, choosing_a_book, reed_book1, reed_book2, logout_user

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', register_user),
    path('login/', login_user, name='login'),
    path('select_books/', choosing_a_book, name='books'),
    path('books/war_and_peace', reed_book1),
    path('books/game_of_the_thrones', reed_book2),
    path('logout/', logout_user, name='logout'),
]
