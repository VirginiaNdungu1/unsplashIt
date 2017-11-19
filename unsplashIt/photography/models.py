from django.db import models
import datetime as dt

# Create your models here.


class Artist(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    username = models.CharField(max_length=30)
    portfolio = models.CharField(max_length=30, blank=True)
    Bio = models.CharField(max_length=30, blank=True)
    phone_number = models.CharField(max_length=20, blank=True)

    def save_artist(self):
        self.save()

    def __str__(self):
        return self.username


class Genre(models.Model):
    name = models.CharField(max_length=30)
    genre_image = models.ImageField(upload_to='genre/')

    def save_genre(self):
        self.save()

    @classmethod
    def get_genres(cls):
        genres = cls.objects.all()
        return genres

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=30)
    tag_image = models.ImageField(upload_to='tags/')

    def save_tag(self):
        self.save()

    def __str__(self):
        return self.name


class Photo(models.Model):
    photo_image = models.ImageField(upload_to='photos/')
    title = models.CharField(max_length=30)
    story = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    genre = models.ForeignKey(Genre)
    artist = models.ForeignKey(Artist)
    tags = models.ManyToManyField(Tag, blank=True)

    def save_photo(self):
        self.save()

    @classmethod
    def get_photos(cls, genre_id):
        photos = cls.objects.filter(genre=genre_id)
        return photos

    @classmethod
    def search_photos_by_title(cls, search_term):
        photos = cls.objects.filter(title__icontains=search_term)
        return photos

    def __str__(self):
        return self.title
