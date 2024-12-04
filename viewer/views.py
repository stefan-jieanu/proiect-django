from django.shortcuts import render
from django.http import HttpResponse
from django.template.defaultfilters import title

from .models import Genre, Movie

# Create your views here.
# def hello(request, param, param2):
#     return HttpResponse(f'<h1>Hello {param}, {param2} World!</h1>')

def hello(request):
    param = request.GET.get('param', '')
    return HttpResponse(f'<h1>Hello {param}</h1>')

def home(request):
    fav_food = ['pizza', 'apple', 'paste']
    user = ''

    return render(
        request,
        template_name='home.html',
        context={'example_var': 1234, 'food': fav_food, 'user': user}
    )

def movies(request):
    movies = Movie.objects.all()

    return render(
        request,
        template_name='movies.html',
        context={'movies': movies}
    )

def movies_detail(request, title):
    movie = Movie.objects.get(title=title)

    return render(
        request,
        template_name='movies_detail.html',
        context={'movie': movie}
    )

# def movies(request):
#     print('All movies:')
#     my_movies = Movie.objects.all()
#     print(my_movies)
#
#     # get() returneaza un singure obiect dupa un criteriu de cautare
#     # obiectul returnat trebuie sa fie unic dupa acel criteriu
#     print('Get movie by name')
#     the_good_place = Movie.objects.get(title='The good place')
#     print(the_good_place.title)
#     print(the_good_place.description)
#
#     # filter() returneaza toate obiectele dupa un anumit criteriu
#     print('Get all movies by rating: ')
#     movies_rating_6 = Movie.objects.filter(rating=6)
#     print(movies_rating_6)
#
#     print('Get all movies with rating greater than 6: ')
#     movies_rating_greater_6 = Movie.objects.filter(rating__gt=6)
#     print(movies_rating_greater_6)
#
#     return HttpResponse(f'<h1>Movies list: </h1>')

# 'title' este un regular expression parameter
# def movies_detail(request, title):
    # Query params
    # request.GET este un dictionar cu query params speicificati in url
    # de exemplu: http://127.0.0.1:8000/movies/my-movie?sort=dupa_titlu in acest link
    # 'sort' este un query param

    # Metoda request.GET.get('numel_param', 'backup') returneaza valoarea unui query param dupa nume
    # Daca nu exista un query param cu acel nume va returna a doua valoare din parametrii
    # Pentru url-ul http://127.0.0.1:8000/movies/my-movie?sort=dupa_titlu&order=a_z
    # 'sort' si 'order' o sa fie parte din dict-ul request.GET
    # sort_by = request.GET.get('sort', 'nu am gasit query params')
    # order = request.GET.get('order', '')

    # return HttpResponse(f'<h1>Movie detail: {title}</h1> <p>Filme sortate: {sort_by}, dupa: {order}<p>')
    # return HttpResponse('Movie detail')