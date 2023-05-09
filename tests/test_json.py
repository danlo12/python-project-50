from gendiff.generate_diff import gen_diff
import json


def test_json():
    assert gen_diff("tests/fixturs/file1.json", "tests/fixturs/file2.json", "JSON") == json.dumps({"    host": "hexlet.io", "  - timeout": 50, "  + timeout": 20, "  - follow": "false", "  - proxy": "123.234.53.22", "  + verbose": "true"})
