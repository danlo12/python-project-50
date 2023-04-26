from gendiff import gen_diff


def test_plain():
    assert gen_diff.generate_diff("tests/fixturs/file2.json", "tests/fixturs/file1.json", "PLAIN") != gen_diff.generate_diff("tests/fixturs/file1.json", "tests/fixturs/file2.json", "PLAIN")
