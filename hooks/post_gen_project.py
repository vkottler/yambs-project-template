"""
post_gen_project - Perform some actions that are not templated.
"""

# built-in
import subprocess
from typing import List


def git_cmd(args: List[str], check: bool = True) -> None:
    """Run a 'git' command."""

    subprocess.run(["git"] + args, check=check)


def mk_cmd(args: List[str], check: bool = True) -> None:
    """Run an 'mk' command."""

    subprocess.run(["mk"] + args, check=check)


def initialize(ssh_url: bool = False) -> None:
    """Initialize a repository, 'config' sub-module."""

    git_cmd(["init"])
    git_cmd(
        [
            "submodule",
            "add",
            "git@github.com:vkottler/config.git"
            if ssh_url
            else "https://github.com/vkottler/config.git",
        ]
    )
    git_cmd(["submodule", "update", "--init", "--recursive"])


def commit() -> None:
    """
    Stage everything and commit, it's okay if committing doesn't work (e.g.
    running in CI).
    """

    git_cmd(["add", "-A"])
    git_cmd(["commit", "-m", "Initial commit."], False)


def datazen() -> None:
    """Run initial datazen sync."""

    # Render everything.
    mk_cmd(["dz-sync"])


initialize()
datazen()
commit()

mk_cmd(["g"])
mk_cmd(["gb"])

# Things that run in CI for these projects.
mk_cmd(["yaml", "python-lint", "python-sa"])

# Run tests.
mk_cmd(["t"])
