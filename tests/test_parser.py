from gendiff import parg

file1 = {
  "host": "hexlet.io",
  "timeout": 50,
  "proxy": "123.234.53.22",
  "follow": False
}
file2 = {
  "timeout": 20,
  "verbose": True,
  "host": "hexlet.io"
}


def test_pars():
    assert parser.definition_form('tests/fixturs/file1.json') == file1
    assert parser.definition_form('tests/fixturs/file1.yaml') == file1
    assert parser.definition_form('tests/fixturs/file2.json') == file2
    assert parser.definition_form('tests/fixturs/file2.yml') == file2
