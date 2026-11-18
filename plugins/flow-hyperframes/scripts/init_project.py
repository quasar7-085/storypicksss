"""Prepare a production workspace, keeping edits and generated media intact."""
import argparse
from pathlib import Path
import shutil


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("project", type=Path, help="Directory for this production")
    root = parser.parse_args().project.resolve()
    resources = Path(__file__).resolve().parents[1] / "resources"
    paths = ["sources", "work", "outputs/planning", "outputs/images/references",
             "outputs/images/storyboards", "outputs/prompts", "outputs/video/scenes",
             "outputs/edit", "outputs/exports"]
    files = {".production/" + name: resources / name for name in
             ("workflow.md", "layout.md", "read_stage.py", "review.py")}
    files[".codex/agents/storyboard_reviewer.toml"] = resources / "storyboard_reviewer.toml"
    for name in [*paths, *files, "work/status.md"]:
        target = root / name
        if root not in target.resolve().parents or target.is_symlink():
            parser.error(f"Project path points outside the workspace or is a link: {name}")
    for name in paths:
        (root / name).mkdir(parents=True, exist_ok=True)
    for name, source in files.items():
        target = root / name
        target.parent.mkdir(parents=True, exist_ok=True)
        if not target.exists():
            with target.open("xb") as dest, source.open("rb") as src:
                shutil.copyfileobj(src, dest)
        elif target.read_bytes() != source.read_bytes():
            print(f"Kept existing project file: {name}")
    status = root / "work/status.md"
    if not status.exists():
        with status.open("x", encoding="utf-8") as dest:
            dest.write("# 제작 진행 기록\n\n현재 단계 · 01 제작 환경 확인 전\n")
    print(root)


if __name__ == "__main__":
    main()
