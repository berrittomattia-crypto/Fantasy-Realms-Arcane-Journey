# Apply the quest override bundle

1. Open the Modrinth App and locate the Fantasy Realms instance.
2. Open the instance folder from its menu.
3. Download the `Fantasy-Realms-Quest-Overrides` artifact from the latest successful **Build quest overrides** GitHub Actions run.
4. Extract the ZIP.
5. Copy the contents of its `overrides/` folder into the root of the Minecraft instance folder.
6. Merge folders and replace files when prompted.
7. Launch the instance and check all six FTB Quests chapters in a new test world first.

Do not delete your existing `saves` folder. The override bundle contains no world save.

The bundle only updates quest/configuration files. The repository does not redistribute the 55 binary mod JARs and does not yet publish a complete standalone `.mrpack`; install the original pack first.
