"""Check built artifacts and commands without downloading models or calling APIs."""
import os
from pathlib import Path
import subprocess
import sys
import tarfile
import tempfile
import unittest
import zipfile


PROJECT = Path(__file__).resolve().parents[1]


class PackagingTests(unittest.TestCase):
    def test_artifact_contents(self):
        wheel, = (PROJECT / "dist").glob("*.whl")
        sdist, = (PROJECT / "dist").glob("*.tar.gz")
        with zipfile.ZipFile(wheel) as archive:
            names = archive.namelist()
            for filename in ["faq.csv", "tickets.db", "telecom_guide.pdf"]:
                self.assertIn(f"telecom_rag_chatbot/data/{filename}", names)
        with tarfile.open(sdist) as archive:
            source_names = archive.getnames()
            self.assertTrue(any(name.endswith("/.env.example") for name in source_names))
            self.assertTrue(any(name.endswith("/uv.lock") for name in source_names))
        for name in names + source_names:
            self.assertFalse(set(Path(name).parts) & {".env", ".venv", "chroma_store", "__pycache__"}, name)

    def test_wheel_works_outside_checkout(self):
        wheel, = (PROJECT / "dist").glob("*.whl")
        with tempfile.TemporaryDirectory() as directory:
            installed = Path(directory) / "installed"
            work = Path(directory) / "work"
            work.mkdir()
            with zipfile.ZipFile(wheel) as archive:
                archive.extractall(installed)
            env = dict(os.environ, PYTHONPATH=str(installed), TELECOM_CHROMA_DIR=str(work / "vectors"))
            code = '''
from pathlib import Path
from telecom_rag_chatbot import config
import csv
import sqlite3
assert Path(config.CHROMA_DIR) == Path.cwd() / "vectors"
with (config.DATA_DIR / "faq.csv").open() as source:
    assert list(csv.DictReader(source))
with sqlite3.connect(f"file:{config.DATA_DIR / 'tickets.db'}?mode=ro", uri=True) as connection:
    assert connection.execute("SELECT count(*) FROM tickets WHERE status = 'resolved'").fetchone()[0]
assert (config.DATA_DIR / "telecom_guide.pdf").read_bytes().startswith(b"%PDF")
'''
            result = subprocess.run([sys.executable, "-c", code], cwd=work, env=env, capture_output=True, text=True)
            self.assertEqual(result.returncode, 0, result.stderr)
            for command in ["chat", "web", "ingest"]:
                result = subprocess.run(
                    [sys.executable, "-c", f"from telecom_rag_chatbot.launcher import {command}; {command}()", "--help"],
                    cwd=work, env=env, capture_output=True, text=True,
                )
                self.assertEqual(result.returncode, 0, result.stderr)
                self.assertIn("usage:", result.stdout)


if __name__ == "__main__":
    unittest.main()
