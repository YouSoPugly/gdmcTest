from gdpc import Editor, lookup, Box, Block

# The block types to search downwards if found at the current position.
BLOCKS = lookup.TREE_BLOCKS | lookup.MUSHROOM_BLOCKS | lookup.AIRS


def log(area: Box, editor: Editor):
    rect = area.toRect()
    x1, z1 = rect.begin
    x2, z2 = rect.end

    worldSlice = editor.loadWorldSlice(rect)
    heightmap = worldSlice.heightmaps.get("MOTION_BLOCKING")

    for x in range(x1, x2):
        for z in range(z1, z2):
            y = heightmap[x - x1, z - z1] - 1
            block = worldSlice.getBlock([x - x1, y, z - z1])
            while block.id in BLOCKS:
                editor.placeBlock([x, y, z], Block("minecraft:air"))
                y -= 1
                block = worldSlice.getBlock([x - x1, y, z - z1])

            if block.id == "minecraft:dirt":
                editor.placeBlock([x, y, z], Block("minecraft:grass_block"))


    return
