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

from reviste.models import Publicatie, Revista
from viewer.models import Genre, Movie

from viewer.views import hello, home, movies, movies_detail, movies_genre

from django.conf import settings
from django.conf.urls.static import static

from reviste.views import hello_reviste, reviste, reviste_detail

admin.site.register(Genre)
admin.site.register(Movie)

admin.site.register(Publicatie)
admin.site.register(Revista)

urlpatterns = [
    path('admin/', admin.site.urls),

    # Regular expressions parameter in url
    # path('hello/<param>/<param2>', hello)

    # Paths for 'viewer' app
    # Parameters for path() function
    # path('path/name', view_name, name='my-page')
    # 'path/name' is the url path we want to define. It can be anything we want but should be represetative of the page
    # view_name is the name of the view function assosiated with that path or page
    # name='my-page' is a special name that we can use to reference this path inside the rest of our project

    path('hello/', hello),
    path('', home, name='home'),
    path('movies/', movies, name='movie-page'),
    path('movies/<title>', movies_detail, name='movies-detail'),
    path('movies/genre/<name>', movies_genre, name='movies-genre'),

    # Paths for 'reviste' app
    path('hello-reviste/', hello_reviste, name='hello-reviste'),
    path('reviste/', reviste, name='reviste-page'),
    path('reviste/<title>', reviste_detail, name='revista-detail'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# ^ adds url for our static files to be made available to the client
# static files are located in a directory named 'static/' in the same folder as the app
# static files are .css/.js files
# when making changes to .css or .js files make sure to reload the page with Ctrl+Shift+R to clear browser cache
