from gendiff import gendiff

def test_plain():
    assert gendiff.generate_diff("tests/fixturs/file2.json", "tests/fixturs/file1.json", "PLAIN") != gendiff.generate_diff("tests/fixturs/file1.json", "tests/fixturs/file2.json", "PLAIN")
