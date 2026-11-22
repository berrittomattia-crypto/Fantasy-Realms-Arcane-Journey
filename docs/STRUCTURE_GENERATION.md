# Structure generation and exploration

This page distinguishes settings carried into the 1.1.0 build from changes newly made for that build.

## Settings in the source profile and retained in 1.1.0

| Mod / setting | Value in the source profile | 1.1.0 action |
|---|---:|---|
| Moog's Voyager Structures — universal frequency multiplier | 0.7 | Retained; no additional per-structure overrides added |
| YUNG's Better Dungeons — small Nether dungeons | Enabled | Retained |
| IDAS — vanilla desert pyramid | Disabled | Retained |
| IDAS — Ice and Fire structure integration | Disabled | Retained |
| IDAS — labyrinth mining fatigue | Enabled | Retained |

Moog's config describes the universal multiplier as a structure-frequency multiplier: 0.7 means the Moog frequency baseline is reduced to 70% before any per-mod or per-structure multipliers are applied. This is not a global multiplier for every structure mod.

## Rare exploration targets

IDAS's default structure sets already place landmark structures less frequently than its common roadside structures. Its rarest tier includes the **Ancient Portal** and **Nexus** (spacing 60, separation 40); those values have not been changed in 1.1.0. See the [IDAS rarity guide](https://mc-wiki.net/idas/idas-structure-rarity-guide/) and [structure overview](https://mc-wiki.net/idas/idas-getting-started-guide/).

The quest text now gives the player a clue to seek the Ancient Portal or Nexus and suggests using the Explorer's Compass, carrying supplies and searching different biomes. The main exploration path also includes the Ancient City, Stronghold, Aether and Otherside branches.

## World-generation caveat

Structure-frequency changes only affect chunks generated after the relevant config/datapack is active. They do not regenerate already explored chunks. Make a new world for the intended distribution, or travel into unexplored terrain in an existing world.

## What has not been changed

- No new per-structure Moog multipliers have been added.
- IDAS spacing/separation values have not been rewritten.
- The Ice and Fire beta port has not been included; IDAS's Ice and Fire structures remain disabled.
- No claim is made that all structure placements have been tested in a fresh world.
