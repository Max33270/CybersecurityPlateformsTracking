import csv
import json
import sys
from collections import defaultdict
from pathlib import Path


def load_directory(directory: Path) -> dict[str, list[dict]]:
    by_user: dict[str, list[dict]] = defaultdict(list)

    for json_file in sorted(directory.glob("*.json")):
        with json_file.open(encoding="utf-8") as f:
            try:
                body = json.load(f)
            except json.JSONDecodeError as e:
                print(f"[warn] Could not parse {json_file.name}: {e}")
                continue

        for item in body.get("data", []):
            if item.get("own_type") == "module_section_own":
                username = item.get("user", {}).get("name", "unknown")
                by_user[username].append(item)
            elif item.get("own_type") == "module_own":
                username = item.get("user", {}).get("name", "unknown")
                by_user[username].append(item)
            elif item.get("own_type") == "machine_root_own":
                username = item.get("user", {}).get("name", "unknown")
                by_user[username].append(item)
            else :
                continue

    return by_user


def write_csv(username: str, items: list[dict], output_dir: Path) -> None:
    sorted_items = sorted(items, key=lambda x: x.get("created_at", ""))

    output_path = output_dir / f"{username}_htb_progression.csv"
    with output_path.open("w", newline="", encoding="utf-8-sig") as f:
        writer = csv.writer(f)
        writer.writerow(["count", "date", "details"])
        for i, item in enumerate(sorted_items, start=1):
            if item.get("own_type") != "machine_root_own" : 
                display_as = item.get("own", {}).get("display_as", "")
                created_at = item.get("created_at", "")
                writer.writerow([i, created_at, display_as])
            else :
                display_as = "Owned Machine "
                display_as += item.get("own", {}).get("name", "")
                created_at = item.get("created_at", "")
                writer.writerow([i, created_at, display_as])

    print(f"  → {output_path.name}  ({len(sorted_items)} entries)")


def main(directory: str) -> None:
    path = Path(directory)
    if not path.is_dir():
        print(f"Error: '{directory}' is not a valid directory.")
        sys.exit(1)

    print(f"Reading JSON files from: {path.resolve()}\n")
    by_user = load_directory(path)

    if not by_user:
        print("No module_section_own entries found.")
        return

    for username, items in by_user.items():
        write_csv(username, items, path)

    print(f"\nDone. {len(by_user)} CSV file(s) written.")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python parse_htb_progression.py <directory>")
        sys.exit(1)
    main(sys.argv[1])