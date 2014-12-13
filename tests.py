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

        self.arch_path = self.make_path("tests_files/.git.zip")

        self._to_rm = []

    def tearDown(self):
        for path in self._to_rm:
            if os.path.exists(path):
                shutil.rmtree(path)

    def remove_dir_on_tear_down(self, path):
        self._to_rm.append(path)

    def add_git_dir_to(self, root):
        git_dir = os.path.join(root, ".git/")
        self.remove_dir_on_tear_down(git_dir)
        if not os.path.exists(git_dir):
            with zipfile.ZipFile(self.arch_path) as a:
                a.extractall(root)
        return git_dir

    def make_path(self, dirname):
        return os.path.abspath(
            os.path.join(os.path.dirname(__file__), dirname)
        )

    def check(self, root, asserter):
        asserter(self.fn(root, short=True), self.short)
        asserter(self.fn(root, short=False), self.long)

    def test_existing(self):
        root = self.make_path("tests_files")
        self.add_git_dir_to(root)
        self.check(root, self.assertEqual)

    def test_non_existing(self):
        root = self.make_path("ne")
        self.check(root, self.assertIsNone)

    def test_root_with_quote(self):
        root = self.make_path("r'oot_dir")
        if not os.path.exists(root):
            os.mkdir(root)
        self.remove_dir_on_tear_down(root)
        self.add_git_dir_to(root)
        self.check(root, self.assertEqual)


if __name__ == "__main__":
    unittest.main()
