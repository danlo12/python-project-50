from gendiff.scripts.gendiff import generate_diff
__all__ = ["generate_diff","build_fixture_path"]

import os.path

FIXTURES_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "fixtures")


def build_fixture_path(file, path=FIXTURES_PATH):
    return os.path.join(path, file)
