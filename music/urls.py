from django.conf.urls import url
from . import views
# namespacing for the urls
app_name = 'music'


urlpatterns = [
    #/music
    url(r'^$', views.IndexView.as_view(), name="index"),

    # /music/album_id/
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name="detail"),
    # adding an album
    url(r'album/add/$', views.AlbumCreate.as_view(), name="album-add"),

    # /music/album_id/favourite
    # url(r'^(?P<album_id>[0-9]+)/favourite/$', views.favourite, name="favourite"),
]
