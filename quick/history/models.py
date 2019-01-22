from django.db import models

class Artist(models.Model):
    artist_name = models.CharField(max_length=200)

    def __str__(self):
      return self.artist_name



class Song(models.Model):
    song_name = models.CharField(max_length=200)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)


    def __str__(self):
      return self.song_name