import vlc
import pafy
import sys


def play(movie):
   instance = vlc.Instance()
       #movie is the YouTube or a local URL
   media = instance.media_new(movie)
   media_list = instance.media_list_new([movie]) #A list of one movie

   player = instance.media_player_new()
   player.set_media(media)

   #Create a new MediaListPlayer instance and associate the player and playlist with it

   list_player =  instance.media_list_player_new()
   list_player.set_media_player(player)
   list_player.set_media_list(media_list) 

url = "http://www.youtube.com/watch?v=0ErKe36lHd0"
video = pafy.new(url).getbest().url
print(video)
play(url)
while True:
    pass
print("done")
