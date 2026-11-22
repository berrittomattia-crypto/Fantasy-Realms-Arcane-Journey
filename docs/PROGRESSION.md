# Progression and quest design

This is the intended design brief. It is not yet a claim that all quests have been implemented in FTB Quests.

## Principles

- Every progression-defining overpowered ability and item is gated by quests.
- Roughly half of non-critical discovery remains open-ended; the quest book gives clues, maps, context and optional routes rather than forcing every activity.
- Rewards scale with risk. Early quests give supplies and small amounts of experience, not late-game weapons or rare boss drops.
- Exploration discovers magic: books, scrolls, relics and materials should be found through structures, dimensions, bosses and crafted research milestones.
- The main narrative is revealed gradually through journals, ruins, NPC-like encounters and boss milestones. The player retains freedom over the order of many discoveries.

## Chapters

### 1. Il Risveglio
**Purpose:** establish survival, first home and the mystery.

Suggested quest chain:
1. Un mondo sconosciuto — first night survived; reward: food and basic supplies.
2. Un riparo — craft a bed and establish a base; reward: basic building materials.
3. Tracce nel fango — gather wood, stone and food; reward: modest XP.
4. Il primo indizio — find a structure or a written clue; reward: explorer's hint/map item, only after validating its item ID.
5. Una bussola per l'ignoto — obtain or craft an Explorer's Compass; explain that it helps locate known structures but does not replace clues.

### 2. Le arti arcane
**Purpose:** introduce magic without making it immediately dominant.

Suggested quest chain:
1. Frammenti d'energia — discover a first arcane material.
2. Il tomo dimenticato — acquire the intended Ars Nouveau entry book through a verified acquisition route.
3. Prime formule — craft a basic spellbook or perform a first spell milestone.
4. Un'altra via — discover Iron's Spells 'n Spellbooks and obtain a low-tier scroll.
5. Il prezzo del potere — complete a modest combat or resource challenge before unlocking better spell progression.

### 3. Il mondo dimenticato
**Purpose:** encourage deliberate structure and dimension exploration.

Suggested quest chain:
1. Pietre fuori posto — discover a notable overworld structure.
2. Archivi sepolti — find a written lore clue in a dungeon.
3. Oltre il cielo — unlock and enter The Aether.
4. L'eco profonda — reach Deeper and Darker content after suitable gear preparation.
5. La mappa incompleta — collect clues from multiple structure families; reward: next-location hint, not an endgame item.

### 4. Le creature leggendarie
**Purpose:** prepare the player for named, high-risk encounters.

Suggested quest chain:
1. Bestiario — record or defeat selected dangerous mobs.
2. Il primo guardiano — defeat an early Cataclysm/Mowzie encounter selected after testing its difficulty.
3. Preparazione — craft a midgame armor/weapon set and stock healing supplies.
4. Il richiamo antico — defeat a major boss; reward: unique crafting material, not the final weapon.
5. Draghi — planned chapter branch; keep disabled until a compatible dragon mod is verified for this exact loader/version.

### 5. L'ascesa
**Purpose:** late-game crafting, boss progression and mastery.

Suggested quest chain:
1. Maestria arcana — complete advanced spell milestones.
2. Reliquie del passato — collect rare materials from multiple regions/dimensions.
3. Prova del titano — defeat a late-game boss.
4. Il sigillo — craft a multi-part key/relic after completing previous milestones.
5. La soglia — unlock the final chapter only after the major progression checks are met.

### 6. Il potere assoluto
**Purpose:** God Wand endgame gate.

Suggested quest chain:
1. Le sei prove — complete the required chapter milestones.
2. L'ultima reliquia — gather rare components from late-game bosses and dimensions.
3. Il cuore del mondo — complete the final boss/story objective.
4. Il potere assoluto — unlock the God Wand only now, through the quest reward or a gated recipe.

## Reward policy

| Stage | Appropriate rewards | Avoid |
|---|---|---|
| Early | food, basic materials, small XP, maps/clues | enchanted high-tier gear, rare boss drops |
| Early magic | low-tier scrolls, starter books, research materials | high-level spells, unlimited mana/production |
| Exploration | map fragments, compasses, lore books, modest supplies | teleport shortcuts to every rare structure |
| Boss milestones | unique crafting ingredients, trophies, controlled gear upgrades | God Wand or equivalent power |
| Final | God Wand after all final checks | early access through loot tables or recipes |

## Implementation requirements before release

1. Inspect the actual FTB Quests SNBT files and preserve stable quest/chapter IDs when editing.
2. Build all six chapter SNBTs with valid task types, item IDs and reward definitions.
3. Ensure God Wand cannot be obtained early from loot, crafting, commands exposed to players, or alternate recipes; keep admin access separate.
4. Verify each reward item ID against the installed mods and test quest completion in a fresh world.
5. Confirm datapacks are detected and enabled, and confirm progression does not break world generation.
6. Test a clean installation and a fresh world before publishing a release.
