# Validation status

## Confirmed from the uploaded source export and its logs

- The source index targets Minecraft 1.21.1 and NeoForge 21.1.265.
- The archive contains 48 indexed mod files plus 7 additional JARs in `overrides/mods` (55 JARs total).
- The bundled runtime log shows NeoForge 21.1.265 loaded, FTB Quests and God Wand present, 6,981 recipes loaded, and 5,261 advancements loaded.
- The log records a session inside the existing `TEST` world and a normal shutdown that saved the overworld, Nether, End and modded dimensions.
- The source FTB Quests configuration contains one chapter (`Il Risveglio`) and one quest object with one item task: collect 16 `minecraft:oak_log`.
- The source KubeJS startup and server scripts are example placeholders; they do not currently gate recipes or implement quest progression.

## Issues visible in the source log

The session did reach the world, but the log is not error-free. Repeated resource reloads account for some duplicate entries.

- **Missing Ice and Fire registry entries:** IDAS loot tables refer to many `iceandfire:` items, and Integrated API reports `iceandfire:dread_lich` as an invalid entity. The source export has Rampart but does not include the Ice and Fire mod itself.
- **Missing optional biome references:** IDAS tags reference `byg:redwood_thicket` and Biomes O' Plenty biomes, but those biome mods are not in the source mod list.
- **GeckoLib animation parse errors:** `attack_single`, `supernova` and `swim_charge` contain expressions that fail to parse because of `nan` values.
- **Other data errors:** the log also contains missing advancement references, an Integrated API spawner parse error tied to the missing Ice and Fire entity, and invalid `minecraft:air` item loads.

## Still required before a stable release

- Test the candidate Ice and Fire port in a separate copy, then check whether it resolves the IDAS loot-table and spawner errors without creating new conflicts.
- Decide whether optional BYG/Biomes O' Plenty integration tags should be removed/disabled or whether those biome mods are actually wanted.
- Trace and repair the GeckoLib animation and invalid item errors.
- Create and verify all six FTB Quests chapters, valid task/reward IDs, quest dependencies and localization.
- Verify that God Wand acquisition is locked behind the final quest. The source config's cooldown/damage/terrain settings are not, by themselves, proof of quest gating.
- Test new-world generation, structures, dimensions, boss progression, performance and a clean installation.

A successful entry into the existing test world is useful evidence, but it is not equivalent to a clean compatibility pass or a stable release.
