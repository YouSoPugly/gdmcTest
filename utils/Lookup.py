from gdpc import lookup

UNNATURAL = lookup.STRUCTURE_BLOCKS
SETTLEMENT_BLOCKS = lookup.CAMPFIRES | lookup.BEDS | lookup.ORNAMENTAL_BLOCKS | lookup.UI_BLOCKS
PATH_BLOCKS = {"minecraft:path_block", "minecraft:gravel", "minecraft:podzol", "minecraft:coarse_dirt",
               "minecraft:packed_mud", "minecraft:rooted_dirt"}
ROAD_BLOCKS = {"minecraft:stone_bricks", "minecraft:smooth_stone"}


OVERWORLD_STONES = lookup.IGNEOUS | {"minecraft:stone"}
OVERWORLD_DIRTS = lookup.OVERWORLD_SOILS - {"minecraft:gravel", "minecraft:farmland"}
OVERWORLD_EARTH = OVERWORLD_DIRTS | OVERWORLD_STONES | {"minecraft:snow_block"}

OCEAN_BIOMES = {"minecraft:ocean", "minecraft:deep_ocean", "minecraft:warm_ocean", "minecraft:lukewarm_ocean",
                "minecraft:deep_lukewarm_ocean", "minecraft:cold_ocean", "minecraft:deep_cold_ocean",
                "minecraft:frozen_ocean", "minecraft:deep_frozen_ocean"}
RIVER_BIOMES = {"minecraft:river", "minecraft:frozen_river"}

PLAINS_BIOMES = {"minecraft:plains", "minecraft:sunflower_plains", "minecraft:beach", "minecraft:wooded_badlands",
                 "minecraft:birch_forest", "minecraft:old_growth_birch_forest", "minecraft:dark_forest",
                 "minecraft:windswept_hills", "minecraft:windswept_gravelly_hills, minecraft:windswept_forest",
                 "minecraft:meadow", "minecraft:cherry_grove", "minecraft:mushroom_fields", "minecraft:forest"}

WETLAND_BIOMES = {"minecraft:swamp", "minecraft:mangrove_swamp"}

TAIGA_BIOMES = {"minecraft:taiga", "minecraft:jagged_peaks", "minecraft:frozen_peaks", "minecraft:stony_peaks",
                "minecraft:grove", "minecraft:snowy_slopes", "minecraft:old_growth_pine_taiga",
                "minecraft:old_growth_spruce_taiga", "minecraft:snowy_taiga", "minecraft:snowy_beach",
                "minecraft:snowy_plains", "minecraft:ice_spikes"}

ARID_BIOMES = {"minecraft:desert", "minecraft:savanna", "minecraft:savanna_plateau", "minecraft:windswept_savanna",
               "minecraft:badlands", "minecraft:eroded_badlands"}

JUNGLE_BIOMES = {"minecraft:jungle", "minecraft:sparse_jungle", "minecraft:bamboo_jungle"}

CAVE_BIOMES = {"minecraft:deep_dark", "minecraft:dripstone_caves", "minecraft:lush_caves"}
