from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    url('^$', views.index, name='welcome'),
    url(r'^genre/(\d+)/$', views.genre, name='genre'),
    url(r'^photos/(\d+)/$', views.photos, name='photo'),
    url(r'^search/$', views.search_photo, name='search_photo')
]
if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
