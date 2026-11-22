# Fantasy Realms — The Arcane Journey

A guided fantasy-adventure modpack for **Minecraft 1.21.1** on **NeoForge 21.1.265**.

> Development status: documentation and progression design are being prepared. The repository is not yet a complete, launch-tested modpack release.

## Design goals

- Exploration-first fantasy adventure with dangerous dungeons, rare structures and meaningful discoveries.
- Magic learned progressively through exploration and quest milestones.
- Boss encounters and legendary rewards reserved for later progression.
- God Wand is an endgame reward, never an early-game item.
- A guided but non-linear story: the player uncovers the world's forgotten history and its growing threat.

## Story chapters

1. **Il Risveglio** — survive, gather supplies and uncover the first signs of an older world.
2. **Le arti arcane** — find the first sources of magic and learn how to use them responsibly.
3. **Il mondo dimenticato** — explore ancient structures, hidden dimensions and lost records.
4. **Le creature leggendarie** — prepare for powerful creatures and major boss encounters.
5. **L'ascesa** — master advanced equipment, magic and the world's greatest challenges.
6. **Il potere assoluto** — the final trials; only here can the God Wand become available.

## Current base pack

The source export inspected for this project contains 48 Modrinth-indexed mod files plus 7 additional mod jars in `overrides/mods` (55 total) and targets:
- Minecraft: 1.21.1
- NeoForge: 21.1.265

See `docs/MODLIST.md` for the exact indexed mod list and `docs/PROGRESSION.md` for the quest design.

## Installation and release status

A tested `.mrpack` release has **not** been published from this repository yet. The source export contained a local test world and session-specific files; those are deliberately excluded from this public repository.

## Repository layout

- `docs/` — mod inventory, progression design and validation notes.
- `pack/` — clean, distributable overrides and pack metadata will be staged here.
- `scripts/` — repeatable validation/build helpers will be added here.
