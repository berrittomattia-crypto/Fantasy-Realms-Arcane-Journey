# FTB Quests — implementation status

## Current state

The uploaded source archive contains **one** FTB Quests chapter, `Il Risveglio`, with one quest and one task: collect 16 oak logs. Its chapter, quest and task IDs are preserved in the audit notes.

The six-chapter story and mission outlines below are a design plan. They are **not** six completed SNBT files, and no 31-quest implementation is currently staged in the repository.

## Target design

1. **Il Risveglio** — survival, shelter, first materials and first clue.
2. **Le arti arcane** — introduce Ars Nouveau and Iron's Spells gradually.
3. **Il mondo dimenticato** — Nether and optional branches for the Ancient City, Stronghold, Aether and Deeper and Darker.
4. **Le creature leggendarie** — preparation, dangerous dungeons and carefully tested boss milestones.
5. **L'ascesa** — advanced magic, Netherite, late-game relics and End progression.
6. **Il potere assoluto** — final trials and the God Wand reward.

The intended design mixes automatic objectives with manual expedition or boss confirmations where reliable identifiers have not yet been verified.

## God Wand gate — not implemented yet

The source export already contains conservative God Wand settings (long cooldowns, terrain damage disabled and PvP disabled). Those settings do not prevent early acquisition.

Still required:
- Remove or gate every player-accessible recipe and loot acquisition path.
- Add the wand as a reward only on the final quest after all required milestones.
- Keep autoclaim disabled so the player must claim it in the quest book.
- Test in a fresh world and verify no alternate acquisition path exists.

No KubeJS quest-gate script has been staged. Do not assume the wand is currently quest-locked.

## Installation

There is no installable quest override ZIP available yet. Do not copy files from the planned structure until actual SNBT and KubeJS overrides have been added and validated.
