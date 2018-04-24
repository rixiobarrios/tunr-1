from django.conf.urls import url

from rest_framework.routers import DefaultRouter

from . import views

urlpatterns = [
  url(r'artists/$', views.ArtistList.as_view(), name='artists-list'),
  url(r'artists/(?P<pk>[0-9]+)/$', views.ArtistDetail.as_view(), name='artist-detail'),
  url(r'songs/$', views.SongList.as_view(), name='songs-list'),
  url(r'songs/(?P<pk>[0-9]+)/$', views.SongDetail.as_view(), name='song-detail')
]
