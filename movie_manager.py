import os
import collections
import random

beta = 2

class MovieManager:
    def __init__(self):
        self.tagged_files = collections.defaultdict(list)
        self.tag_responses = dict()
        self.process_files("./movies")

    def process_files(self, path):
        files = os.listdir(path)
        for movie in files:
            name, tags = movie.split("-")
            tags,_ = tags.split(".")
            tags = tags.split(",")
            for tag in tags:
                self.tagged_files[tag.strip()].append(movie)
                self.tag_responses[tag] = 1

    def tag_positive_response(self, tag, tag_value):
        '''
        0 < tag value < 1
        '''
        self.tag_responses[tag] *= tag_value * beta

    def tag_negative_response(self,tag,tag_value):
        '''
        0 < tag_value < 1
        '''
        self.tag_responses[tag] /= tag_value * beta

    def tag_video_reaction(self, filename, reaction):
        '''
        -1 < reaction < 1
        '''
        for tag, files in self.tagged_files.items():
            if filename in files:
                if reaction > 0:
                    self.tag_positive_response(tag, reaction)
                if reaction < 0:
                    self.tag_negative_response(tag, reaction)


    def choose_video(self):
        total_ratings = sum(self.tag_responses.values())
        p = random.random() * total_ratings
        running_rating_sum = 0
        for tag, rating in  self.tag_responses.items():
            running_rating_sum += rating
            if (running_rating_sum > p):
                return random.choice(self.tagged_files[tag])

    def __str__(self):
        return str(self.tagged_files) + "\n" + str(self.tag_responses)
