from gdpc import Editor, Block

import numpy as np

from utils.Heightmap import get_heightmap


def draw_border(editor: Editor):
    area = editor.getBuildArea()
    heightmap = get_heightmap(area)

    y = heightmap.max() + 10

    for z in range(area.begin.z, area.end.z+1):
        editor.placeBlock([area.begin.x, y, z], Block("minecraft:black_wool"))
        editor.placeBlock([area.end.x, y, z], Block("minecraft:black_wool"))

    for x in range(area.begin.x, area.end.x):
        editor.placeBlock([x, y, area.begin.z], Block("minecraft:black_wool"))
        editor.placeBlock([x, y, area.end.z], Block("minecraft:black_wool"))
