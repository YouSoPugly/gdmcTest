import numpy as np
from gdpc import Editor, Box


class Settlement:
    def __init__(self, editor: Editor, area: Box):
        self.editor = editor
        self.slice = editor.loadWorldSlice(area.toRect())
        self.area = area

        self.map = np.zeros((area.size.x, area.size.z))
        self.biomes = np.zeros((area.size.x, area.size.z)).astype(str)
        self.structures = []

    def generate(self):
        pass

    def search_biomes(self):
        hmap = self.slice.heightmaps["MOTION_BLOCKING_NO_LEAVES"]
        for x in range(self.area.size.x):
            for z in range(self.area.size.z):
                y = hmap[x, z]
                self.biomes[x, z] = self.slice.getBiome([x, y, z])

        return self.biomes
