from django.conf.urls import url

from rest_framework.routers import DefaultRouter

from . import views

urlpatterns = [
  url(r'artists/$', views.ArtistList.as_view()),
  url(r'artists/(?P<pk>[0-9]+)/$', views.ArtistDetail.as_view())
]
