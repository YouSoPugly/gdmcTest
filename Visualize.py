"""A script that displays a height map of the build area."""

import matplotlib.pyplot as plt
import numpy as np
import time

from gdpc import Editor, lookup

from utils.Heightmap import get_heightmap


def visualize():

    heightmap = get_heightmap(Editor().getBuildArea())

    # normalize the heightmap to the range [0, 255]
    heightmap = (heightmap - heightmap.min()) * 255 / (heightmap.max() - heightmap.min())
    heightmap = heightmap.clip(0, 255).astype(np.uint8)

    plt.imshow(heightmap, cmap='gray')
    plt.show()
