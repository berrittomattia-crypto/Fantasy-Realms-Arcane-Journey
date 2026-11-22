# Progression and quest design

This is the design brief for the campaign, not a record of already implemented quests.

## Principles

- Every overpowered item or progression-defining ability is gated by quests.
- Roughly half of non-critical discoveries remain open-ended; quests give clues, maps and hints rather than forcing every activity.
- Rewards scale with risk. Early quests give food, materials and modest XP, not late-game weapons.
- Magic is discovered through books, structures, dimensions and research milestones.
- The main narrative unfolds gradually; the order of many discoveries remains flexible.

## Chapters

### 1. Il Risveglio
Survival, first shelter, wood/stone/iron milestones and the first clue to the world's hidden history.

### 2. Le arti arcane
Discover arcane materials, acquire the entry books for Ars Nouveau and Iron's Spells through verified routes, craft basic spell equipment and complete a first magic expedition.

### 3. Il mondo dimenticato
Explore the Nether and then pursue optional branches such as an Ancient City, Stronghold, Aether expedition or Deeper and Darker expedition. Require multiple branch milestones rather than one rigid route.

### 4. Le creature leggendarie
Prepare with suitable armor and healing supplies, then face selected Cataclysm and Mowzie encounters. Exact boss objectives must be checked against entity IDs and playtested difficulty before being made automatic.

### 5. L'ascesa
Advanced magic, Netherite, rare relics, a Nether Star and the Ender Dragon milestone. Balance rewards against the installed mod versions.

### 6. Il potere assoluto
Complete the final trials, gather rare materials and defeat the final challenge before receiving the God Wand.

## Reward policy

| Stage | Appropriate rewards | Avoid |
|---|---|---|
| Early | food, basic materials, modest XP | enchanted high-tier gear |
| Early magic | starter research materials and low-tier scrolls | high-level spells and unlimited production |
| Exploration | clues, maps, modest supplies | universal structure teleport shortcuts |
| Boss milestones | trophies and controlled upgrade materials | God Wand |
| Final | God Wand after all final milestones | early recipe or loot access |

## Implementation checklist

1. Generate valid FTB Quests SNBT for installed FTB Quests 2101.1.39.
2. Preserve original chapter/quest/task IDs where possible.
3. Verify item, advancement, structure, dimension and entity identifiers.
4. Add and validate the God Wand recipe/loot gate and final reward.
5. Test quest completion and rewards in a fresh world.
6. Test generation, structures, dimensions and boss progression before release.
