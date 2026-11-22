# Static dependency check — locally bundled override jars

This report is based on the `META-INF/neoforge.mods.toml` files extracted from the seven jars in `overrides/mods`, cross-checked against the exact base mod versions listed in the Modrinth index. It is a **static metadata check**, not a runtime launch test.

Target environment: Minecraft 1.21.1, NeoForge 21.1.265.

| Mod ID | Installed version | Declared required dependencies | Static result |
|---|---:|---|---|
| `ars_n_spells` | 3.4.2 | NeoForge 21.1.x; Minecraft 1.21.1; Ars Nouveau 5.13.x; Iron's Spells 3.16.3 up to but not including 4.0 (optional) | Passes declared ranges: Ars Nouveau 5.13.5 and Iron's Spells 3.16.4 are present |
| `ftblibrary` | 2101.1.40 | NeoForge 21.1+; Minecraft 1.21.1+; Architectury 13.0.11+ | Passes: NeoForge 21.1.265, Minecraft 1.21.1, Architectury 13.0.12 |
| `ftbquests` | 2101.1.39 | NeoForge 21.1+; Minecraft 1.21.1+; Architectury 13.0.11+; FTB Library 2101.1.40+; FTB Teams 2101.1.9+ | Passes: all required versions are present |
| `ftbteams` | 2101.1.12 | NeoForge 21.1+; Minecraft 1.21.1+; Architectury 13.0.8+; FTB Library 2101.1.37+ | Passes: all required versions are present |
| `godwand` | 1.6.2 | NeoForge 21.1.72+; Minecraft 1.21.1 | Passes the declared loader/game ranges |
| `rampart` | 1.1.0 | NeoForge 21.1.197+; Minecraft 1.21.1 | Passes the declared loader/game ranges |
| `resonant_arcana` | 1.2.2 | NeoForge 21.1.219–21.1.x; Minecraft 1.21.1; Iron's Spells 3.16.3 up to but not including 3.17 | Passes: Iron's Spells 3.16.4 is present |

## Notes

- FTB Quests' required FTB Library and FTB Teams dependencies are both present at versions meeting the jar's declared minimums.
- Ars 'n Spells requires Ars Nouveau 5.13+ and treats Iron's Spells as optional; both are present at versions in the declared ranges.
- Resonant Arcana requires Iron's Spells 3.16.x and the installed 3.16.4 fits its range.
- Rampart is included but no current bundled mod manifest declares it as required. It is useful as the dependency for the Ice and Fire port candidate, but **Rampart alone does not add dragons**.
- This check does not validate every mod from the Modrinth index, runtime mixin compatibility, generated world structures, performance, or quest script behavior.

## Dragon candidate

A community Ice and Fire port now publishes a Minecraft 1.21.1 NeoForge beta. Its instructions require Rampart 1.1.0+ and NeoForge 21.1.197+; the source export already includes Rampart 1.1.0 and uses NeoForge 21.1.265. This is a promising dependency fit, but it remains a beta and still needs an isolated load test and fresh-world test before being included in a stable pack. See [the port's compatibility matrix](https://github.com/Vladeezyy/IceAndFire) and [the 1.21.1 NeoForge beta file](https://www.curseforge.com/minecraft/mc-mods/ice-and-fire-unofficial-port/files/9666230).
