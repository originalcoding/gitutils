import os
import shutil
import zipfile
import unittest


class VersionGetterTest(unittest.TestCase):

    def setUp(self):
        from gitutils import get_head_hash
        self.fn = get_head_hash
        self.short = "6339b2b"
        self.long = "6339b2b6509a3ee8fbf6eed9f1741bfd6ac3030f"
        self.root = os.path.abspath(
            os.path.join(
                os.path.dirname(__file__),
                "tests_files/",
            )
        )

        self.git_dir = os.path.join(self.root, ".git/")

        if not os.path.exists(self.git_dir):
            with zipfile.ZipFile(os.path.join(self.root, ".git.zip")) as a:
                a.extractall(self.root)

    def tearDown(self):
        if os.path.exists(self.git_dir):
            shutil.rmtree(self.git_dir)

    def test_existing(self):
        short, long = (
            self.fn(self.root, short=True),
            self.fn(self.root, short=False),
        )
        self.assertEqual(short, self.short)
        self.assertEqual(long, self.long)

    def test_non_existing(self):
        ne = os.path.abspath(
            os.path.join(
                os.path.dirname(__file__),
                "ne/",
            )
        )
        self.assertIsNone(self.fn(ne, short=True))
        self.assertIsNone(self.fn(ne, short=False))


if __name__ == "__main__":
    unittest.main()

