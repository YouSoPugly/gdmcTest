import numpy
from gdpc import Editor
from matplotlib import pyplot as plt

import generators.Terrain.Terraform as Terraform
import generators.Terrain.Logger as Logger
import generators.Debug as Debug

import utils.Noise as Noise

import numpy as np


def test():
    editor = Editor(buffering=True, bufferLimit=100)
    editor.runCommand("gamerule doTileDrops false")
    Logger.log(editor.getBuildArea(), editor)
    Terraform.clear_foliage(editor.getBuildArea(), editor)
    editor.runCommand("gamerule doTileDrops true")

    Debug.draw_border(editor)
    editor.flushBuffer()


def noise_test():
    SIZE = 100
    nmap = numpy.zeros((SIZE, SIZE))

    noise = Noise.Noise(10, 3)

    for x in range(0, SIZE):
        for z in range(0, SIZE):
            nmap[x, z] = noise.get_value(x, z)

    # normalize the nmap to the range [0, 255]
    nmap = (nmap - nmap.min()) * 255 / (nmap.max() - nmap.min())
    nmap = nmap.clip(0, 255).astype(np.uint8)

    plt.imshow(nmap, cmap='gray')
    plt.show()


if __name__ == '__main__':
    #test()
    noise_test()
