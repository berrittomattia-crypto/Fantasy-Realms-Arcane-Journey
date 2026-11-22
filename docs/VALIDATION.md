# Validation status

## Inspected

- Source Modrinth pack index: Minecraft 1.21.1, NeoForge 21.1.265, 48 indexed mod files.
- Source export includes local `saves/TEST`, Xaero map data for `TEST`, launcher logs, client options and user/session cache files. Those are not copied into this public repository.
- Source includes FTB Quests config paths and an `il_risveglio.snbt` chapter file; the full quests data must be reviewed before making any claim about quest completion or gating.
- Source includes God Wand server configuration, KubeJS scripts and mod configs. They require inspection and controlled edits before being treated as final.

## Not yet validated

- Full Minecraft launch and new-world creation.
- All mod interactions and world generation at runtime.
- Exact FTB Quests task/reward behavior.
- God Wand recipe and loot gating.
- Dragon content for this exact loader/version.
- Performance on the user's hardware.

A release must not be labeled stable until these checks pass.
