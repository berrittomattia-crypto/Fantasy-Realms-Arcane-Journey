#!/usr/bin/env python3
"""Static checks for the Fantasy Realms FTB Quests staging files."""
from __future__ import annotations
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
QUESTS = ROOT / "pack/overrides/config/ftbquests/quests"
CHAPTERS = QUESTS / "chapters"
ALLOWED_TYPES = {"item", "checkmark", "advancement", "dimension", "structure", "kill", "xp_levels"}
ID_RE = re.compile(r'\bid: "([A-F0-9]{16})"')
QUEST_RE = re.compile(r'\{\s*id: "([A-F0-9]{16})"\s+x:')
DEP_RE = re.compile(r'dependencies: \[(.*?)\]', re.S)
TYPE_RE = re.compile(r'\btype: "([a-z_]+)"')


def balanced_snbt(path: Path) -> bool:
    text = path.read_text(encoding="utf-8")
    braces = brackets = 0
    quoted = escaped = False
    for char in text:
        if quoted:
            if escaped:
                escaped = False
            elif char == "\\":
                escaped = True
            elif char == '"':
                quoted = False
            continue
        if char == '"':
            quoted = True
        elif char == "{":
            braces += 1
        elif char == "}":
            braces -= 1
        elif char == "[":
            brackets += 1
        elif char == "]":
            brackets -= 1
        if braces < 0 or brackets < 0:
            return False
    return not quoted and braces == 0 and brackets == 0


def main() -> int:
    errors: list[str] = []
    files = sorted(CHAPTERS.glob("*.snbt"))
    if len(files) != 6:
        errors.append(f"Expected 6 chapter files, found {len(files)}")

    all_ids: list[str] = []
    quest_ids: set[str] = set()
    dependencies: list[str] = []
    task_types: set[str] = set()
    for path in files:
        if not balanced_snbt(path):
            errors.append(f"Unbalanced SNBT: {path.relative_to(ROOT)}")
        text = path.read_text(encoding="utf-8")
        all_ids.extend(ID_RE.findall(text))
        quest_ids.update(QUEST_RE.findall(text))
        for block in DEP_RE.findall(text):
            dependencies.extend(re.findall(r'"([A-F0-9]{16})"', block))
        task_types.update(TYPE_RE.findall(text))

    if len(all_ids) != len(set(all_ids)):
        errors.append("Duplicate 16-character IDs found in chapter files")
    missing = sorted(set(dependencies) - quest_ids)
    if missing:
        errors.append(f"Dependencies reference missing quest IDs: {missing}")
    unknown_types = sorted(task_types - ALLOWED_TYPES)
    if unknown_types:
        errors.append(f"Unknown task/reward types: {unknown_types}")

    for locale in ("en_us", "it_it"):
        path = QUESTS / "lang" / f"{locale}.snbt"
        if not path.exists() or not balanced_snbt(path):
            errors.append(f"Missing or unbalanced locale file: {path.relative_to(ROOT)}")

    manifest_path = ROOT / "pack/quests-manifest.json"
    if not manifest_path.exists():
        errors.append("Missing quests-manifest.json")
    else:
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        if len(manifest) != 31:
            errors.append(f"Expected 31 quests in manifest, found {len(manifest)}")
        if {item["quest_id"] for item in manifest} != quest_ids:
            errors.append("Manifest quest IDs do not match chapter files")

    first = (CHAPTERS / "il_risveglio.snbt").read_text(encoding="utf-8")
    for preserved_id in ("729446B24249BFB0", "1C6141CF87219243", "6DC4D5B357953164"):
        if preserved_id not in first:
            errors.append(f"Original FTB Quest ID was not preserved: {preserved_id}")
    if not re.search(r'id: "6DC4D5B357953164"[\s\S]{0,250}?count: 16L', first):
        errors.append("Original oak-log task count is not serialized as an SNBT long")

    final_chapter = (CHAPTERS / "il_potere_assoluto.snbt").read_text(encoding="utf-8")
    wand_occurrences = sum(path.read_text(encoding="utf-8").count("godwand:god_wand") for path in files)
    if wand_occurrences != 3 or "godwand:god_wand" not in final_chapter:
        errors.append("God Wand should appear only as final chapter/quest icon and final reward")
    gate = ROOT / "pack/overrides/kubejs/server_scripts/fantasy_godwand_gate.js"
    if not gate.exists() or "event.remove({ output: 'godwand:god_wand' })" not in gate.read_text(encoding="utf-8"):
        errors.append("God Wand recipe-removal script is missing or malformed")

    if errors:
        print("FAIL")
        for err in errors:
            print("-", err)
        return 1

    print("PASS")
    print(f"Chapters: {len(files)}")
    print(f"Quests: {len(quest_ids)}")
    print(f"Unique chapter/task/reward IDs: {len(all_ids)}")
    print(f"Task/reward type tags: {', '.join(sorted(task_types))}")
    print("Dependencies: all targets exist")
    print("Translations: en_us and it_it present")
    print("God Wand: final chapter reward + recipe removal script present")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
