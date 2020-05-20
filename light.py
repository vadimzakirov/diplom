from entropy_base import Entropy
import wave
import numpy as np
import matplotlib.pyplot as plt
import math


class LightEntropy(Entropy):

    def __init__(self):
        super(LightEntropy, self).__init__()
        #self.list = [1,1,1,1,1,1,1,0,0,0,0,0,0,0,1,0,1,0,1,1,1,1,0]
    def make_list_from_file(self):
        with open("entropy_inputs/coordinates_not_ideal.txt", "r") as f:
            str = f.read()
            coordinates = str.split(",")
            coordinates[-1] = '0'
            print(coordinates)
        int_coordinates = []
        for coordinate in coordinates:
            if coordinate != '0':
                int_coordinates.append(int(coordinate))
                self.coordinates.append(int(coordinate))
        print(int_coordinates)
        for elem in int_coordinates:
            if elem > 250:
                self.list.append(1)
            else:
                self.list.append(0)

    def make_hist(self):
        n, bins, patches = plt.hist(self.coordinates, 10, facecolor='blue', alpha=0.5)
        plt.savefig("light_outputs/2_full_elem_hist.png", dpi=72)



LE = LightEntropy()
LE.make_list_from_file()
LE.count()
LE.make_binary_file()