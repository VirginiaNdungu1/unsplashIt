from django.contrib import admin
from .models import Artist, Genre, Tag, Photo


class PhotoAdmin(admin.ModelAdmin):
    filter_horizontal = ('tags',)


# Register your models here.
admin.site.register(Artist)
admin.site.register(Genre)
admin.site.register(Tag)
admin.site.register(Photo, PhotoAdmin)
