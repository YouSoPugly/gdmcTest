from gdpc import lookup

UNNATURAL = lookup.STRUCTURE_BLOCKS
SETTLEMENT_BLOCKS = lookup.CAMPFIRES | lookup.BEDS | lookup.ORNAMENTAL_BLOCKS | lookup.UI_BLOCKS
PATH_BLOCKS = {"minecraft:path_block", "minecraft:gravel", "minecraft:podzol", "minecraft:coarse_dirt", "minecraft:packed_mud", "minecraft:rooted_dirt"}
ROAD_BLOCKS = {"minecraft:stone_bricks", "minecraft:smooth_stone"}


OVERWORLD_STONES = lookup.IGNEOUS | "minecraft:stone"
OVERWORLD_DIRTS = lookup.OVERWORLD_SOILS - {"minecraft:gravel", "minecraft:farmland"}
OVERWORLD_EARTH = OVERWORLD_DIRTS | OVERWORLD_STONES | "minecraft:snow_block"
