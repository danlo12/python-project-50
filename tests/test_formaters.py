from gendiff import gendiff
from tests import build_fixture_path
import pytest


@pytest.mark.parametrize("custom_format,expected,file1,file2",
                         [("JSON", "json_right_result", "file1.json", "file2.json"),
                          ("PLAIN", "plain_right_result", "file1.json", "file2.json"),
                          ("STYLISH", "stylish_right_result", "file1.json", "file2.json")])
def test_plain_and_json(custom_format, expected, file1, file2):
    with open(build_fixture_path(expected)) as expected_file:
        expected_content = expected_file.read()
        assert gendiff.generate_diff(build_fixture_path(file1),
                                     build_fixture_path(file2), custom_format) == expected_content
