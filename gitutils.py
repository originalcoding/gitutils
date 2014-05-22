"""Git-related utilities."""

__version__ = "0.1"
__author__ = "Original Coding"


import os
import shlex
import subprocess


def get_head_hash(root, short=False):
    root = os.path.normpath(root)

    git_dir = os.path.join(root, ".git/")

    if not os.path.isdir(git_dir):
        return

    bits = ["git"]
    bits.append("--git-dir='{}'".format(git_dir))
    bits.append("rev-parse")
    if short:
        bits.append("--short")
    bits.append("HEAD")

    cmd = shlex.split(" ".join(bits))

    try:
        output = subprocess.check_output(cmd, universal_newlines=True)
    except (subprocess.CalledProcessError, OSError):
        return

    return output.strip()

