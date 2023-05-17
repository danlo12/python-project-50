from tests.fixturs import right_result
from gendiff import gendiff


def test_gendiff():
    assert right_result.right_stylish() == gendiff.generate_diff('tests/fixturs/file1.json', 'tests/fixturs/file2.json')
