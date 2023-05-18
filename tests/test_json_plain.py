from gendiff import gendiff
import pytest

test_input_plain = gendiff.generate_diff("tests/fixturs/file2.json", "tests/fixturs/file1.json", "PLAIN")
right_plain = open("tests/fixturs/plain_right_result")
right_plain = right_plain.read()
test_input_json = (gendiff.generate_diff("tests/fixturs/file1.json", "tests/fixturs/file2.json", "JSON"))
right_json = open("tests/fixturs/json_right_result")
right_json = right_json.read()


@pytest.mark.parametrize("test_input,expected", [(test_input_json, right_json), (test_input_plain, right_plain)])
def test_plain_and_json(test_input, expected):
    assert test_input == expected
