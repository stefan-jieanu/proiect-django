"""
URL configuration for hollymovies project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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

from viewer.models import Genre, Movie

from viewer.views import hello, home, movies, movies_detail, movies_genre

from django.conf import settings
from django.conf.urls.static import static

admin.site.register(Genre)
admin.site.register(Movie)

urlpatterns = [
    path('admin/', admin.site.urls),

    # Regular expressions parameter in url
    # path('hello/<param>/<param2>', hello)

    path('hello/', hello),
    path('', home, name='home'),
    path('movies/', movies, name='movie-page'),
    path('movies/<title>', movies_detail, name='movies-detail'),
    path('movies/genre/<name>', movies_genre, name='movies-genre')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
