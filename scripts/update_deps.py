#!/usr/bin/env python3

from shutil import which
from subprocess import run
from sys import stderr

POETRY = "poetry"
R2F = "req2flatpak"


def command_exists(name: str) -> bool:
    return which(name) is not None


def error(s: str):
    stderr.write(s + "\n")


def main() -> None:
    if not command_exists("pip"):
        error("Pip not found. Install it first.")
        exit(1)
    if not command_exists("req2flatpak"):
        r2f_pip = run(["pip", "install", "req2flatpak"])
        if r2f_pip.returncode != 0:
            error("Error installing req2flatpak")
            exit(1)
    poetry_export = run(
        [POETRY, "export", "--without-hashes", "-o", "requirements.txt"]
    )
    if poetry_export.returncode != 0:
        error("Error in exporting python dependencies.")
        exit(1)
    r2f = run(
        [
            R2F,
            "-r",
            "requirements.txt",
            "-o",
            "python-dependencies.json",
            "-t",
            "cp310-aarch64",
            "cp310-x86_64",
        ]
    )
    if r2f.returncode != 0:
        error("Error in exporting Flatpak Module dependencies")
        exit(1)
    exit(0)


if __name__ == "__main__":
    main()
