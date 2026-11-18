import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


class ProjectTest(unittest.TestCase):
    def test_init_and_resume(self):
        plugin = Path(__file__).resolve().parents[1] / "plugins/flow-hyperframes"
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "첫 작품"
            init = [sys.executable, str(plugin / "scripts/init_project.py"), str(root)]
            subprocess.run(init, check=True, capture_output=True)
            status = root / "work/status.md"
            status.write_text("03A 채택", encoding="utf-8")
            board = root / "outputs/images/storyboards/s03a-board-v01.png"
            board.touch()
            subprocess.run(init, check=True, capture_output=True)
            self.assertEqual(status.read_text(encoding="utf-8"), "03A 채택")
            self.assertTrue(board.is_file())
            self.assertTrue((root / ".codex/agents/storyboard_reviewer.toml").is_file())
            for stage in range(1, 16):
                output = subprocess.check_output(
                    [sys.executable, str(root / ".production/read_stage.py"), str(stage)],
                    text=True, encoding="utf-8"
                )
                self.assertTrue(output.startswith(f"## {stage:02d}. "))


if __name__ == "__main__":
    unittest.main()
