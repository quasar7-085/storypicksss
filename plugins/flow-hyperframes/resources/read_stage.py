"""Print the shared rules or one stage of the short-form production guide."""

import argparse
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("stage", choices=["rules"] + [str(n) for n in range(1, 16)])
    stage = parser.parse_args().stage
    root = Path(__file__).resolve().parent
    guide = root / "workflow.md"
    heading = "## AI 실행 규칙" if stage == "rules" else f"## {int(stage):02d}. "
    found = False
    with guide.open(encoding="utf-8") as source:
        for line in source:
            if line.startswith("## "):
                if found:
                    break
                found = line.startswith(heading)
            if found:
                print(line, end="")
    if not found:
        parser.error(f"Section missing: {heading}")


if __name__ == "__main__":
    main()
