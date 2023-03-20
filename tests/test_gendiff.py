from tests.fixturs import right_result
from gendiff import generate_diff


def test_gendiff():
    file_list = {
        '- follow': False,
        '  host': 'hexlet.io',
        '- proxy': '123.234.53.22',
        '- timeout': 50,
        '+ timeout': 20,
        '+ verbose': True}
    assert generate_diff.mk_str(file_list) == right_result.right()
    assert right_result.right() == generate_diff.generate_result('tests/fixturs/file1.json', 'tests/fixturs/file2.json')
