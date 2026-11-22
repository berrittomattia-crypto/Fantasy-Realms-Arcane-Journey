# 1.1.0 validation report

## Passed checks

- Modrinth archive was generated with Minecraft 1.21.1 and NeoForge 21.1.265 metadata.
- The Modrinth index contains 48 indexed mod files.
- Seven additional mod JARs are bundled under overrides/mods.
- Archive integrity check passed; there are no duplicate ZIP paths.
- No saves/, logs/, Xaero map cache, options.txt, player/session cache or old world data are included.
- Six FTB Quests chapters parse with the local SNBT structural validator.
- Quest counts: 31 quests, 39 tasks, 53 rewards.
- IDs: 129 unique chapter/quest/task/reward IDs.
- Dependency graph: all 36 dependency references target existing quest IDs.
- Original first chapter, first quest and first oak-log task IDs are preserved.
- Italian and English quest locale files contain all chapter and quest title entries.
- Exactly one God Wand reward exists, on the final quest.
- KubeJS recipe-removal script is present and uses the ServerEvents.recipes / event.remove({ output: ... }) API supported by the installed KubeJS 2101.7.2 family.
- Structure configs parse; Moog remains 0.7, YUNG small Nether dungeons are enabled and the IDAS toggles are preserved.

## Not tested in-game

- Importing into the Modrinth App and first launch on the user's PC.
- Fresh-world generation with all structure mods active.
- Visual layout and quest progression in the FTB Quests GUI.
- Actual completion/claiming of all automatic and manual tasks.
- KubeJS removal of the God Wand recipe after server reload.
- God Wand final reward claim and alternate acquisition audit in a running world.
- Performance on the user's hardware.

## Known issues inherited from the 1.0.0 source profile

The source log records a successful entry into the existing TEST world, but also records:
- IDAS loot/spawner references to Ice and Fire items/entities not registered in the source profile.
- IDAS references to optional BYG and Biomes O' Plenty biome IDs not present in the source list.
- GeckoLib animation parsing errors involving NaN values.
- Additional missing advancement and invalid-air item references.

These are documented, not represented as fixed by this package.

## Dragons

A beta Ice and Fire NeoForge 1.21.1 port was identified as a candidate; it is not included because it could not be validated here. Rampart is bundled, but Rampart alone does not add dragons.
