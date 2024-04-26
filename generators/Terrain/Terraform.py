from gdpc import Editor, lookup, Box, Block


def smooth(area: Box):
    return


FOLIAGE = lookup.OVERWORLD_PLANT_BLOCKS | lookup.OVERWORLD_PLANTS - lookup.TREES - lookup.GRASS_BLOCKS


def clear_foliage(area: Box, editor: Editor):
    editor.flushBuffer()

    rect = area.toRect()
    x1, z1 = rect.begin
    x2, z2 = rect.end

    worldSlice = editor.loadWorldSlice(rect)
    heightmap = worldSlice.heightmaps.get("MOTION_BLOCKING")

    for x in range(x1, x2):
        for z in range(z1, z2):
            y = heightmap[x - x1, z - z1]
            if worldSlice.getBlock([x - x1, y - 1, z - z1]).id in FOLIAGE:
                y -= 1
            block = worldSlice.getBlock([x - x1, y, z - z1])
            while block.id in FOLIAGE:
                editor.placeBlock([x, y, z], Block("minecraft:air"))
                y += 1
                block = worldSlice.getBlock([x - x1, y, z - z1])