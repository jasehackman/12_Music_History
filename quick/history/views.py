from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Artist, Song


def index(request):
    artist_list = Artist.objects.all()
    context = {'artist_list': artist_list}
    return render(request, 'history/index.html', context)
    # return HttpResponse(f"We made it!")

def details(request, id):
  # print("LOOK HERE", request.POST['artist'])
  song_list = Song.objects.filter(artist_id = id)
  artist = Artist.objects.get(pk=id)
  context = {'song_list': song_list, 'artist': artist}
  return render(request, 'history/details.html', context)


def newArtist(request):

  artist = Artist(artist_name = request.POST['artist'])
  artist.save()
  added_artist = Artist.objects.filter(artist_name = request.POST['artist'])

  print("added artist", str(added_artist[0].id))
  # args=([value],) must be a tupple
  return HttpResponseRedirect(reverse('history:details', args=(added_artist[0].id,)))


def newSong(request):
  artistId = Artist.objects.get(artist_name=request.POST['artist'])
  print("artistId", artistId.id)
  song = Song(song_name = request.POST['song'], artist_id=artistId.id)
  song.save()
  return HttpResponseRedirect(reverse('history:details', args=(artistId.id, )))
  # print("SONG", song)

def deleteSong(request, songId):
  print(songId)