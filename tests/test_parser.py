from gendiff import parser


def test_pars():
    assert parser.format_definition('tests/fixturs/file1.json') == parser.format_definition('tests/fixturs/file1.yaml')
    assert parser.format_definition('tests/fixturs/file2.json') == parser.format_definition('tests/fixturs/file2.yml')
