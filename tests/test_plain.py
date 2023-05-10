from gendiff import generate_diff


def test_plain():
    assert generate_diff.generate_diff("tests/fixturs/file2.json", "tests/fixturs/file1.json", "PLAIN") != generate_diff.generate_diff("tests/fixturs/file1.json", "tests/fixturs/file2.json", "PLAIN")
