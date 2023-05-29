from gendiff import gendiff
import pytest
import os.path

def find_path(file):
    path = "tests/fixturs/"
    return os.path.join(path,file)


@pytest.mark.parametrize("test_input,expected,file1,file2", [("JSON", "json_right_result","file1.json","file2.json"), ("PLAIN", "plain_right_result","file1.json","file2.json"), ("STYLISH", "stylish_right_result","file1.json","file2.json")])
def test_plain_and_json(test_input, expected,file1,file2):
    expected = open(find_path(expected))
    assert gendiff.generate_diff(find_path(file1), find_path(file2), test_input) == expected.read()
