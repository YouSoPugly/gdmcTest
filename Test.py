import cv2
import numpy
from gdpc import Editor, vector_tools as vt
from matplotlib import pyplot as plt

import generators.terrain.Terraform as Terraform
import generators.terrain.Logger as Logger
import generators.Debug as Debug

import utils.Noise as Noise

import numpy as np

from generators.Settlement import Settlement
from utils import Lookup


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


def biome_test():
    editor = Editor()
    settlement = Settlement(editor, editor.getBuildArea())

    biomes = settlement.search_biomes()

    bmap = np.zeros((settlement.area.size.x, settlement.area.size.z), dtype=int)
    for (x, z), biome in np.ndenumerate(biomes):
        max = settlement.area.size.x - 1  #inverts the x-axis for a proper image
        if biome in Lookup.PLAINS_BIOMES:
            bmap[(max - x, z)] = 0x43F04F
        if biome in Lookup.JUNGLE_BIOMES:
            bmap[(max - x, z)] = 0x21A61C
        if biome in Lookup.ARID_BIOMES:
            bmap[(max - x, z)] = 0xC2ED18
        if biome in Lookup.TAIGA_BIOMES:
            bmap[(max - x, z)] = 0xC2E0ED
        if biome in Lookup.RIVER_BIOMES:
            bmap[(max - x, z)] = 0x15C9ED
        if biome in Lookup.OCEAN_BIOMES:
            bmap[(max - x, z)] = 0x181FED
        if biome in Lookup.CAVE_BIOMES:
            bmap[(max - x, z)] = 0x777777

    bmap = cv2.merge(((bmap) & 0xff, (bmap >> 8) & 0xff, (bmap >> 16) & 0xff))
    bmap = bmap.clip(0, 256)
    bmap = bmap.astype(np.uint8)

    bmap = np.transpose(bmap, (1, 0, 2))
    plt_img = cv2.cvtColor(bmap, cv2.COLOR_RGB2BGR)

    plt.axis('off')

    plt.imshow(plt_img, origin='lower')
    plt.show()


if __name__ == '__main__':
    #test()
    biome_test()
