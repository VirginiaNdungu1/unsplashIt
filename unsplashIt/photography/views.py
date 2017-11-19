from django.shortcuts import render
from django.http import Http404
import datetime as dt
from .models import Artist, Genre, Tag, Photo

# Create your views here.


def index(request):
    genres = Genre.get_genres()
    # genre = Genre.objects.get(id=genre_id)

    return render(request, 'photography_base/index.html', {"genres": genres, })


# def genre(request, genre_id):
#     try:
#         genre = Genre.objects.get(id=genre_id)
#     except DoesNotExist:
#         raise Http404()
#     return render(request, 'photography_base/index.html', {"genre": genre})


def genre(request, genre_id):
    try:
        genre = Genre.objects.get(id=genre_id)
        photos = Photo.get_photos(genre)
    except DoesNotExist:
        raise Http404()
    return render(request, 'pictures/genre.html', {"genre": genre, "photos": photos})


def photos(request, photo_id):
    try:
        # genre = Genre.objects.get(id=genre_id)
        photo = Photo.objects.get(id=photo_id)
    except DoesNotExist:
        raise Http404()
    return render(request, 'pictures/photo.html', {"photo": photo})


def search_photo(request):
    if 'photo' in request.GET and request.GET["photo"]:
        search_term = request.GET.get("photo")
        searched_photos = Photo.search_photos_by_title(search_term)
        message = f"{search_term}"
        return render(request, "pictures/search.html", {"photos": searched_photos, "message": message})
    else:
        message = "No search results yet...."
        return render(request, 'pictures/search.html', {"message": message})
