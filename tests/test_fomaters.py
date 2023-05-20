from gendiff import gendiff
import pytest


def find_path(file):
    file = "tests/fixturs/" + file
    return file


@pytest.mark.parametrize("test_input,expected", [("JSON", "json_right_result"), ("PLAIN", "plain_right_result"), ("STYLISH", "stylish_right_result")])
def test_plain_and_json(test_input, expected):
    expected = open(find_path(expected))
    assert gendiff.generate_diff("tests/fixturs/file1.json", "tests/fixturs/file2.json", test_input) == expected.read()
