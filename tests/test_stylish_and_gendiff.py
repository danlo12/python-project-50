
from gendiff import gendiff


def test_gendiff():
    right_result = open("tests/fixturs/stylish_right_result")
    right_result = right_result.read()
    assert gendiff.generate_diff('tests/fixturs/file1.json', 'tests/fixturs/file2.json') == right_result
