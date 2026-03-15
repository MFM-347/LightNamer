import unittest
from pathlib import Path

from lightnamer.core import LightNamer


class TestLightNamer(unittest.TestCase):
    def setUp(self):
        self.lightnamer = LightNamer(debug=True)
        self.test_dir = Path("test_files")
        self.test_dir.mkdir(exist_ok=True)

        for i in range(3):
            (self.test_dir / f"file_{i}.txt").touch()

    def tearDown(self):
        for file in self.test_dir.iterdir():
            file.unlink()
        self.test_dir.rmdir()

    def test_get_sorted_files(self):
        files = self.lightnamer.sortFn(self.test_dir, order="alphabet")
        self.assertEqual(len(files), 3)

    def test_rename_files_simulation(self):
        self.lightnamer.renFn("Test", self.test_dir, order="alphabet", simulate=True)
