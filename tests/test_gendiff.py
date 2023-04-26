from tests.fixturs import right_result
from gendiff import gen_diff


def test_gendiff():
    assert right_result.right_stylish() == gen_diff.generate_diff('tests/fixturs/file1.json', 'tests/fixturs/file2.json')

