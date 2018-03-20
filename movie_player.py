import moviepy
from moviepy.editor import *
import moviepy.video.fx.all as vfx
import os
import pygame


def play_movie(filename):
    clip = VideoFileClip('./movies/' + filename,target_resolution=(640,480),audio=False,resize_algorithm="fast_bilinear")
    clip.preview(fps=30, audio=False)


