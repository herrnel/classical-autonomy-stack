from abc import ABC, abstractmethod

class Observation:

    def __init__(self, image, front_range_m, timestamp):
        self.__image = image
        self.__front_range_m = front_range_m
        self.__timestamp = timestamp


    def get_image(self):
        return self.__image

    def get_front_range_m(self):
        return self.__front_range_m
    
    def get_timestamp(self):
        return self.__timestamp
