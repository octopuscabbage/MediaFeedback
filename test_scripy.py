import movie_manager
import movie_player


manager = movie_manager.MovieManager()
print(manager)

movie = manager.choose_video()

print(movie)

movie_player.play_movie(movie)
manager.tag_video_reaction(movie,1)
print(manager)
