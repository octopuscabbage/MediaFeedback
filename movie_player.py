import os
import subprocess


def play_movie(youtube_url):
    subprocess.call(["vlc",youtube_url,"--play-and-exit", "--no-video-title-show","-f"])
