# FTB Quests — implementation

This quest pack targets the FTB Quests version **2101.1.39** included in the source export.

## Contents

- 6 chapters matching the agreed story.
- 31 quests, 39 tasks and 51 rewards.
- Italian (`it_it`) and English (`en_us`) chapter/quest localization.
- Explicit dependency graph with visible lock icons.
- Flexible progression: the Nether is mandatory in chapter 3, then at least two of four exploration branches are needed (Ancient City, Stronghold, Aether, Deeper and Darker).
- The original first chapter, first quest and first oak-log task IDs are preserved.

## Chapters

1. **Il Risveglio** — gather oak logs, build a shelter, reach the iron milestone, survive hostile mobs and find the first clue.
2. **Le arti arcane** — collect amethyst and a book, learn Ars Nouveau and Iron's Spells, enchant an item and complete a magic expedition.
3. **Il mondo dimenticato** — enter the Nether, then complete at least two of four optional discoveries: Ancient City, Stronghold, Aether and Deeper and Darker.
4. **Le creature leggendarie** — prepare diamond equipment, hunt Endermen and Blazes, then record victories against Cataclysm/Mowzie bosses and a major dungeon.
5. **L'ascesa** — acquire Blaze Rods, Netherite, Echo Shards and a Nether Star, then defeat the Ender Dragon.
6. **Il potere assoluto** — complete the final trials, gather the last relic materials and complete a final boss/dungeon challenge. The final quest grants one God Wand.

## Task types

Collection of items, vanilla advancements, vanilla hostile mob kills, dimension visits and vanilla structure discoveries are automatic task types. Some boss and expedition objectives are deliberately manual checkmarks because the installed mod versions do not provide one verified common boss identifier for those broad challenges. A checkmark should only be completed after performing the described survival challenge.

## God Wand gate

- KubeJS removes the crafting recipe with output `godwand:god_wand`.
- The God Wand is only awarded by the final quest in chapter 6.
- FTB Quests autoclaim remains disabled, so the reward must be claimed in the quest book after meeting every dependency and the final manual challenge.
- This is a static configuration check. KubeJS recipe removal and final reward behavior still require an in-game test.

## Apply to an existing instance

Copy the contents of `pack/overrides/` into the root of the existing Modrinth instance folder, merging folders and replacing files when prompted. Do not copy any `saves/TEST`, Xaero cache, `options.txt`, player/session caches, command history or logs from the original export.

Back up an existing world before changing quest data. The first chapter/quest/task IDs are retained to reduce the chance of losing existing progress, but the new progression graph should first be tested on a copy or a fresh world.
