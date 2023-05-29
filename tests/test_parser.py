from gendiff import parser


def test_pars():
    assert parser.define_format('tests/fixturs/file1.json') == parser.define_format('tests/fixturs/file1.yaml')
    assert parser.define_format('tests/fixturs/file2.json') == parser.define_format('tests/fixturs/file2.yml')
