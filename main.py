import movie_manager
import movie_player
import headset
import math
import matplotlib.pyplot as plt
from plot_pie import plot_tags

headset = headset.Headset()

manager = movie_manager.MovieManager()

def rating_function(x):
    return math.tanh((x - 40) / 10)

while True:
    print(manager)

    movie = manager.choose_video()

    print(movie)

    movie_player.play_movie(movie)
    print(headset.report_average())
    rating = rating_function(headset.report_average())
    print("Rating: %f" % (rating))
    manager.tag_video_reaction(movie, rating)
    headset.reset_attention_reading()
    plt.clf()
    plot_tags(manager.tag_responses)
    plt.pause(0.05)
plt.show()

