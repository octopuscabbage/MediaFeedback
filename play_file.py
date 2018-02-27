import moviepy
from moviepy.editor import *
import moviepy.video.fx.all as vfx
import os
import pygame


clip = VideoFileClip('test.mp4',target_resolution=(640,480),audio=False,resize_algorithm="fast_bilinear")
clip = clip.fx(vfx.blackwhite)
clip.preview(fps=30, audio=False)


