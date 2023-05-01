from tests.fixturs import right_result
from gendiff import generate_json
from gendiff import gen_diff
def test_json():
    assert right_result.right_json() == gen_diff.generate_diff('tests/fixturs/file1.json', 'tests/fixturs/file2.json', "JSON")