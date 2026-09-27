import tempfile
import unittest
from pathlib import Path

from main import analyze_lab


class AnalyzeLabTests(unittest.TestCase):
    def test_counts_files_directories_size_and_extensions(self):
        with tempfile.TemporaryDirectory() as temporary_directory:
            lab_directory = Path(temporary_directory)
            (lab_directory / "raw").mkdir()
            (lab_directory / "raw" / "sample.csv").write_text("a,b\n1,2\n")
            (lab_directory / "notes").write_text("sample notes")

            report = analyze_lab(lab_directory)

        self.assertEqual(report["files"], 2)
        self.assertEqual(report["directories"], 1)
        self.assertEqual(report["total_size"], 20)
        self.assertEqual(report["extensions"][".csv"], 1)
        self.assertEqual(report["extensions"]["no extension"], 1)


if __name__ == "__main__":
    unittest.main()
