import os.path
__all__ = ["build_fixture_path"]
FIXTURES_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "fixtures")


def build_fixture_path(file, path=FIXTURES_PATH):
    return os.path.join(path, file)
