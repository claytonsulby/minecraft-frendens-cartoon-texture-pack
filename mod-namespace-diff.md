# Mod Namespace Cross-Pack Diff

Compares all non-`minecraft` asset namespaces across packs in `.packs/` that share them.
.DS_Store files are excluded throughout.

---

## Namespace inventory

| Namespace | remix-1.13.2 | remix-1.19 | remix-15w47c(+) |
|---|---|---|---|
| `aether_legacy` | ✓ | ✓ | ✓ |
| `aether_legacy_addon` | ✓ | ✓ | — |
| `lost_aether` | ✓ | ✓ | — |
| `netherchest` | ✓ | ✓ | — |
| `netherex` | ✓ | ✓ | — |
| `omnis_aged_aether_blocks` | ✓ | ✓ | — |
| `totemexpansion` | ✓ | ✓ | — |

`meringued-pack-1.9.4` has no `assets/` directory.
`meringued-pack-15w47c(+)` and `template-1.21.11` have only `minecraft` — no mod namespaces.

---

## `aether_legacy`

### remix-pack-1.13.2 vs remix-pack-1.19

These two are nearly identical. Minor divergence:

#### Only in remix-1.13.2 (1 item)
- `textures/entities/cockatrice/_cockatrice` *(folder — older naming convention)*

#### Only in remix-1.19 (1 item)
- `textures/entities/cockatrice/cockatrice_emis.png` *(emission map, added in 1.19 version)*

#### Files with different content (37 files)
Primarily texture revisions across blocks, entities, items, and GUI:

- **Blocks:** `aerogel.png`, `aether_grass_side/top.png`, `aether_portal.png`, `ambrosium_block.png`, `enchanted_aether_grass_side/top.png`, `golden_oak_leaves.png`, `golden_oak_log_side.png`, `skyroot_bookshelf.png`, `sun_altar_side/top.png`
- **Entities:** `cockatrice/cockatrice.png`, `flying_cow/flying_cow.png`, `flying_cow/saddle.png`, `flying_cow/wings.png`, `phyg/phyg.png`, `phyg/wings.png`, `swet/swet_blue.png`, `swet/swet_golden.png`
- **GUI:** `gui/inventory/accessories.png`
- **Items:** `accessories/agility_cape.png`, `accessories/cape_color_base.png`, `accessories/swet_cape.png`, `food/blue_gummy_swet.png`, `food/golden_gummy_swet.png`, `food/healing_stone.png`, `misc/ambrosium_shard.png`, `misc/golden_amber.png`, `misc/swetty_ball.png`, `misc/zanite_gemstone.png`, `music/aether_tune.png`, `tools/phoenix_shovel.png`, `weapons/jeb_hammer.png`, `weapons/phoenix_sword.png`
- **Tile entities:** `tile_entities/treasure_chest.png`

**Interpretation:** remix-1.13.2 and remix-1.19 are nearly equivalent — remix-1.19 receives one new emission map and has updated textures for 37 assets. One is a direct evolution of the other.

---

### remix-pack-1.13.2 vs remix-pack-15w47c(+)

Dramatic divergence. The 15w47c(+) version is a much older, stripped-down build.

#### Only in remix-1.13.2 (~200+ items)
All the expanded blockstate JSON files, models, lore text files, armor textures, and extra item/texture assets added in the modern builds. Key categories:
- **Blockstates:** 20 new block type entries (levers, beds, trapdoors, signs, doors, panes, bars…)
- **Lore:** 24 `.txt` lore files for items/blocks
- **Models/block + item:** ~80 model JSON files
- **Armor:** 14 accessory armor overlay PNGs + layer 1/2 armor PNGs for 6+ armor sets
- **Blocks:** emissive maps, door/trapdoor textures, crafting table faces, ladder, misc extras
- **Items:** accessories (gloves, capes, rings, shields), armor pieces, food emissives, tools, weapons
- **Tile entities:** skyroot sign, bed, chest subdirectories, tile entity resources folder

#### Only in remix-15w47c(+) (8 items)
- `textures/items/food/berry stem.png`
- `textures/items/food/healing_stone copy.png`
- `textures/items/food/healing_stone_alt.png`
- `textures/items/misc/lore_book stuff.png`
- `textures/tile_entities/large chest fill.png`
- `textures/tile_entities/normal.png`
- `textures/tile_entities/normal_double.png`
- `textures/tile_entities/small chest fill.png`

These appear to be scratch/WIP files (spaces in filenames, `copy.png` suffix) from the older build.

#### Files with different content (37 files)
Same 37-file set as the 1.13.2 vs 1.19 comparison — these are the shared base textures that have been revised across all three versions.

**Interpretation:** remix-15w47c(+) is a legacy snapshot of `aether_legacy` — it contains only the foundational textures plus a handful of leftover scratch files. The 1.13.2 and 1.19 versions are a significant superset, adding full blockstate/model support and a large number of additional textures.

---

### remix-pack-1.19 vs remix-pack-15w47c(+)

Identical relationship to 1.13.2 vs 15w47c(+) above. Only difference: 1.19 has `cockatrice_emis.png` instead of the `_cockatrice` folder. The 37 shared-but-different files are the same set.

---

## `aether_legacy_addon`

### remix-pack-1.13.2 vs remix-pack-1.19

**Identical.** No differences of any kind.

---

## `lost_aether`

### remix-pack-1.13.2 vs remix-pack-1.19

#### Only in remix-1.19 (2 items)
- `structures/platinum_dungeon/New folder` *(empty WIP folder)*
- `structures/platinum_dungeon/backups` *(backup folder)*

**Interpretation:** Essentially identical. remix-1.19 has two leftover work-in-progress/backup folders that carry no texture assets. Non-meaningful.

---

## `netherchest`

### remix-pack-1.13.2 vs remix-pack-1.19

**Identical.** No differences of any kind.

---

## `netherex`

### remix-pack-1.13.2 vs remix-pack-1.19

#### Only in remix-1.19 (3 items)
- `particles/` *(folder)*
- `sounds/entity/` *(folder)*
- `textures/mob_effect/` *(folder)*

**Interpretation:** remix-1.19 extends the `netherex` namespace with three additional resource categories (particles, entity sounds, mob effect icons). remix-1.13.2 is a subset.

---

## `omnis_aged_aether_blocks`

### remix-pack-1.13.2 vs remix-pack-1.19

**Identical.** No differences of any kind.

---

## `totemexpansion`

### remix-pack-1.13.2 vs remix-pack-1.19

**Identical.** No differences of any kind.

---

## Summary

| Namespace | remix-1.13.2 vs remix-1.19 | Notes |
|---|---|---|
| `aether_legacy` | 37 textures revised, 1 file each unique | 1.19 is a direct evolution of 1.13.2; both are a large superset of 15w47c(+) |
| `aether_legacy_addon` | **Identical** | Shared exactly |
| `lost_aether` | Near-identical (2 WIP folders in 1.19) | Non-meaningful |
| `netherchest` | **Identical** | Shared exactly |
| `netherex` | 1.19 is a superset (3 extra folders) | Particles, sounds, mob effects added |
| `omnis_aged_aether_blocks` | **Identical** | Shared exactly |
| `totemexpansion` | **Identical** | Shared exactly |

**Overall:** remix-1.13.2 and remix-1.19 are nearly identical across all mod namespaces — the main differences are ~37 texture revisions in `aether_legacy` and the `netherex` extension in 1.19. remix-15w47c(+) carries only a stripped-down `aether_legacy` namespace (no other mods), with no blockstate/model support and a handful of scratch files that appear to be pre-cleanup leftovers.
