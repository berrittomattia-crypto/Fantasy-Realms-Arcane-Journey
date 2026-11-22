# FTB Quests — 1.1.0 campaign

## Implemented in the 1.1.0 package

- **6 chapters**
- **31 quests**
- **39 tasks**
- **53 rewards**
- Italian and English quest localization
- 129 unique chapter, quest, task and reward IDs
- 36 dependency links, including an optional exploration branch gate that accepts one completed route
- The original chapter, first quest and first oak-log task IDs are preserved for migration compatibility.

## Chapters

1. **Il Risveglio** — survival, shelter, first resources and first signs of the wider world.
2. **Le arti arcane** — a gradual introduction to Ars Nouveau and Iron's Spells.
3. **Il mondo dimenticato** — Nether, Ancient City, Stronghold, Aether and Otherside expeditions.
4. **Le creature leggendarie** — preparation, dangerous creatures, Cataclysm/Mowzie boss trials and major dungeons.
5. **L'ascesa** — Blaze, Echo Shards, Netherite, Wither and Ender Dragon progression.
6. **Il potere assoluto** — final relics and the final God Wand reward.

Some modded boss/expedition milestones are manual checkmarks: the player confirms them only after completing the described challenge. The quest text includes clues for the rare IDAS Ancient Portal and Nexus rather than making the player search every structure blindly.

## God Wand

- The KubeJS server script removes the standard crafting recipe with output godwand:god_wand.
- One God Wand is awarded by the final quest in chapter 6.
- FTB Quests autoclaim remains disabled; the final reward must be claimed in the quest book.
- The source God Wand JAR contains a crafting recipe for that output; the 1.1.0 KubeJS recipe filter is written for the installed KubeJS 2101.7.2 line.

This is statically verified in the package, not runtime-tested in Minecraft. A fresh-world check is still required to prove the recipe is removed and the final reward is claimable in-game.

## Runtime caveat

The imported source log proves that the original profile reached the existing TEST world, but it also contains missing optional registry references and GeckoLib animation errors. The 1.1.0 package is structurally built and statically validated; a new-world runtime test has not been performed.
