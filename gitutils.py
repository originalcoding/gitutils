"""Git-related library."""

__version__ = "0.1.1"
__author__ = "Original Coding"


import os
import subprocess


def get_head_hash(root, short=False):
    root = os.path.normpath(root)

    git_dir = os.path.join(root, ".git/")
    if not os.path.isdir(git_dir):
        return

    bits = ["git", "--git-dir", git_dir, "rev-parse"]
    if short:
        bits.append("--short")
    bits.append("HEAD")

    try:
        output = subprocess.check_output(bits, universal_newlines=True)
    except (subprocess.CalledProcessError, OSError):
        return

    return output.strip()
