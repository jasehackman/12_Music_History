from django.urls import path

from . import views

app_name="history"

urlpatterns = [
  path('', views.index, name='index'),
  path('<int:id>/', views.details, name='details'),
  path('newArtist', views.newArtist, name='newArtist'),
  path('newSong', views.newSong, name='newSong'),
  path('deleteSong', views.deleteSong, name='deleteSong')

]