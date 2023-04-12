from tests.fixturs import right_result
from gendiff import generate_stylish


def test_gendiff():
    assert right_result.right_one() == generate_diff.return_result('tests/fixturs/file1.json', 'tests/fixturs/file2.json')

