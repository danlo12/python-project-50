from gendiff import gendiff
import pytest
import os.path
TESTS_DIR = os.path.dirname(os.path.abspath(__file__))
FIXTURES_PATH = f"{TESTS_DIR}/fixtures"


def build_fixture_path(file, path=FIXTURES_PATH):
    return os.path.join(path, file)


@pytest.mark.parametrize("test_input,expected,file1,file2", [("JSON", "json_right_result", "file1.json", "file2.json"), ("PLAIN", "plain_right_result", "file1.json", "file2.json"), ("STYLISH", "stylish_right_result", "file1.json", "file2.json")])
def test_plain_and_json(test_input, expected, file1, file2):
    with open(build_fixture_path(expected)) as expected_file:
        expected_content = expected_file.read()
        print(expected_content)
        assert gendiff.generate_diff(build_fixture_path(file1), build_fixture_path(file2), test_input) == expected_content
