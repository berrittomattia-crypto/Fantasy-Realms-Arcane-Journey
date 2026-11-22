# Source export audit — 1.0.0

This page records what was actually present in the uploaded `Fantasy Realms – The Arcane Journey 1.0.0.mrpack`, rather than the intended future design.

## Pack contents

- `modrinth.index.json`: 48 indexed mod files.
- `overrides/mods/`: 7 additional local JAR files (Ars 'n Spells, FTB Library, FTB Quests, FTB Teams, God Wand, Rampart and Resonant Arcana).
- Total: 55 mod JARs.
- Runtime target: Minecraft 1.21.1, NeoForge 21.1.265.

## Quest state in the source

- `chapter_groups.snbt` contains an empty chapter-group list.
- `data.snbt` has `progression_mode: "linear"` and autoclaim rewards disabled.
- The only chapter file is `chapters/il_risveglio.snbt`.
- That chapter is titled `Il Risveglio` and contains one quest object with a single item task for 16 oak logs.
- No other story chapter files are present in the source export.

Therefore, the six chapter names in `PROGRESSION.md` are a design plan, not pre-existing implemented quests.

## Existing gameplay tuning in the source

The uploaded export already contains these settings:

- God Wand: cooldown multiplier 2.0, global terrain damage off, PvP off, and major skills such as Supernova, Atomic, Fuga, Gate and Purple set to 3,600-tick cooldowns. The damage values for some abilities remain extremely high. These are balance settings, not proof of quest-locked acquisition.
- Explorer's Compass: creative/cheat teleport disabled, 20 repeat searches, radius 20,000, search cost 2 XP levels, durability 10.
- Moog's Structures: universal frequency multiplier 0.7.
- Iron's Spells: maximum equipment upgrades 2, scroll recycling chance 0.35, wandering-trader magic trades off, mana regeneration multiplier 0.85, spell terrain griefing off.
- Ars Nouveau: no automatic book on login, increased Drygmy mana/progress costs, production quantity cap 3, base armor repair rate 0.
- Aether: no entry starting loot, no repeated Sun Spirit dialogue, and promotional message off.
- IDAS: the config disables its Ice and Fire structures, but several IDAS loot tables and a spawner list still refer to Ice and Fire content. The missing registry references are visible in the runtime log.

## Runtime evidence

The included `overrides/logs/latest.log` records a session that loaded the mod list, loaded 6,981 recipes and 5,261 advancements, entered the existing `TEST` world, and shut down after saving all dimensions.

The log also records repeated errors:
- IDAS loot tables cannot resolve Ice and Fire item IDs.
- Integrated API cannot resolve `iceandfire:dread_lich` for an IDAS spawner.
- Some IDAS biome tags reference BYG and Biomes O' Plenty biome IDs not provided by the current mod list.
- GeckoLib cannot parse the `attack_single`, `supernova` and `swim_charge` animations because expressions contain `nan`.
- There are additional missing advancement references and invalid-air item loads.

This shows the profile can reach a world, but does not constitute a clean validation pass.

## Privacy and distribution

The source export also contains a complete local `saves/TEST` world, Xaero map data for that world, player/session caches, launcher logs and client settings. Those files must not be copied into a public release. The public repository keeps only intentionally curated documentation and pack files.
