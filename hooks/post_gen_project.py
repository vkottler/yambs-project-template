"""
post_gen_project - Perform some actions that are not templated.
"""

# built-in
from os import environ, pathsep
from pathlib import Path
import subprocess
from typing import List

IS_EMBEDDED = "{{cookiecutter.embedded}}" == "True"


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


def remove_conditionals() -> None:
    """Remove some files depending on configuration."""

    if not IS_EMBEDDED:
        for path in [Path("src", "retarget.c")]:
            path.unlink()


initialize()
datazen()
remove_conditionals()
commit()

BASE = []

if IS_EMBEDDED:
    mk_cmd(["download-toolchains"])

    # Add toolchains to PATH.
    environ["PATH"] = (
        str(Path("toolchains", "arm-picolibc-eabi", "bin"))
        + pathsep
        + environ["PATH"]
    )

    BASE.append("variant={{cookiecutter.project_name}}")

mk_cmd(["g"] + BASE)
mk_cmd(["gb"] + BASE)
mk_cmd(["dist", "docs"] + BASE)

# Things that run in CI for these projects.
mk_cmd(["yaml", "python-lint", "python-sa"])

# Run tests.
if not IS_EMBEDDED:
    mk_cmd(["t", "variant=clang", "coverage=false"])
    mk_cmd(["t"])
else:
    subprocess.run(["ninja", "format"], check=True)

subprocess.run(["ninja", "all", "format-check"], check=True)

if not IS_EMBEDDED:
    mk_cmd(["t"])
