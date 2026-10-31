import importlib.util
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
spec = importlib.util.spec_from_file_location("check_repo", ROOT / "tools" / "check_repo.py")
check_repo = importlib.util.module_from_spec(spec)
spec.loader.exec_module(check_repo)


class RepoTest(unittest.TestCase):
    def test_checks_pass(self):
        total, text = check_repo.report()
        self.assertEqual(total, 0, f"repo checks failed:\n{text}")

    def test_capture_is_current(self):
        expected = (ROOT / "assets" / "checks.txt").read_text(encoding="utf-8")
        _, text = check_repo.report()
        self.assertEqual(text, expected, "assets/checks.txt is stale; run python3 tools/check_repo.py --capture assets/checks.txt")


if __name__ == "__main__":
    unittest.main()
