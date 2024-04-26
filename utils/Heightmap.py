from gdpc import Editor, lookup, Box

# The block types to search downwards if found at the current position.
DOWN = lookup.AIRS | lookup.WATERS | lookup.TREE_BLOCKS | lookup.PLANTS | lookup.WOOLS


def get_heightmap(area: Box):
    editor = Editor()

    # see if a different build area was defined ingame
    rect = area.toRect()
    x1, z1 = rect.begin
    x2, z2 = rect.end

    # load the world data and extract the heightmap(s)
    worldSlice = editor.loadWorldSlice(rect)
    heightmap = worldSlice.heightmaps.get("MOTION_BLOCKING_NO_LEAVES")

    for x in range(x1, x2):
        for z in range(z1, z2):
            block = worldSlice.getBlock([x - x1, heightmap[x - x1, z - z1], z - z1])
            while block.id in DOWN:
                heightmap[x - x1, z - z1] -= 1
                block = worldSlice.getBlock([x - x1, heightmap[x - x1, z - z1], z - z1])

    return heightmap
