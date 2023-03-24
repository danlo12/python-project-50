from gendiff import generate_diff

file = {
    "    host": "hexlet.io",
    "  - timeout": "50",
    "  + timeout": "20",
    "  - follow": "false",
    "  - proxy": "123.234.53.22",
    "  + verbose": "true",
  }


def right_one():
    return generate_diff.stulish(file)
