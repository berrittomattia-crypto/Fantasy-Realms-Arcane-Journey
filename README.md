# Fantasy Realms — The Arcane Journey

A guided fantasy-adventure modpack for **Minecraft 1.21.1** on **NeoForge 21.1.265**.

> Current status: source audit and design documentation are in the repository. The curated playable quest/configuration overlay and a tested standalone release are **not yet complete**.

## Design goals

- Exploration-first fantasy adventure with rare structures, dungeons and meaningful discoveries.
- Magic learned progressively through exploration and quest milestones.
- Boss encounters and legendary rewards reserved for later progression.
- God Wand as an endgame reward, not an early-game item.
- A guided but non-linear story revealed through clues, ruins and major encounters.

## Story chapters

1. **Il Risveglio**
2. **Le arti arcane**
3. **Il mondo dimenticato**
4. **Le creature leggendarie**
5. **L'ascesa**
6. **Il potere assoluto**

These are the agreed chapter concepts; the complete six-chapter FTB Quests files have not yet been published.

## Source pack

The inspected source export contains 48 Modrinth-indexed mod files plus 7 additional JARs in `overrides/mods` (55 total), targeting Minecraft 1.21.1 and NeoForge 21.1.265.

See `docs/MODLIST.md`, `docs/DEPENDENCIES.md`, `docs/SOURCE_EXPORT_AUDIT.md`, `docs/PROGRESSION.md` and `docs/FTB_QUESTS.md`.

## Release status

The uploaded export records a successful session entering the existing `TEST` world, but its log contains registry, missing-content and animation errors. A clean fresh-world compatibility pass has not been completed.

No final `.mrpack` or installable quest overlay is published yet. The local test world, Xaero map cache, launcher/session caches and personal files are deliberately excluded from this public repository.
