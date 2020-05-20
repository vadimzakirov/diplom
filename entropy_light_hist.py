

import tk
import wave
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import math
x_y = []
with open(r"coordinates.txt", "r") as file:
    for line in file:
        x_y.append(int(line))
num_bins = 50
DPI = 72
n, bins, patches = plt.hist(x_y, num_bins, facecolor='blue', alpha=0.5)
plt.savefig("light_hist.png", dpi=DPI)
plt.show()
