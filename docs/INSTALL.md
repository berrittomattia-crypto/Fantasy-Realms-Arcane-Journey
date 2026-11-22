# Install Fantasy Realms 1.1.0

The 1.1.0 .mrpack is a complete Modrinth-format profile archive for Minecraft 1.21.1 / NeoForge 21.1.265.

1. Download Fantasy-Realms-Arcane-Journey-1.1.0.mrpack from the file attached to the ChatGPT response.
2. Open the Modrinth App.
3. Choose Create new instance / Import from file (wording may vary by app version).
4. Select the downloaded .mrpack file and let Modrinth install the profile.
5. Launch once and create a new test world before moving any existing world into it.

The profile's Modrinth index contains 48 indexed mod files; seven additional JARs are included in the archive under overrides/mods.

## Existing worlds

The 1.1.0 archive deliberately excludes the old TEST world, Xaero map cache, logs, player/session cache and personal client options. It creates a clean separate profile; it does not overwrite the original instance. Back up your original instance and world before migrating a save.

## Validation status

Archive integrity and static quest/config checks pass. The profile has not been launched in a fresh world as part of this build. The source profile had known optional-content and GeckoLib errors; see docs/VALIDATION.md.

## Dragon note

The Ice and Fire 1.21.1 NeoForge port candidate is beta and is not bundled in 1.1.0. Rampart is included, but that alone does not add dragons.
