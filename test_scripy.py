import movie_manager
import movie_player
import headset
import math

headset = headset.Headset()

manager = movie_manager.MovieManager()

while True:
    print(manager)

    movie = manager.choose_video()

    print(movie)

    movie_player.play_movie(movie)
    print(headset.report_average())
    rating = math.tanh((headset.report_average() - 50) / 10)
    rating = 1;
    print("Rating: %f" % (rating))
    manager.tag_video_reaction(movie, rating)
    headset.reset_attention_reading()
