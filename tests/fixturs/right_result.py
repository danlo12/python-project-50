from gendiff import generate_stylish
from gendiff import gen_diff
file = {
    "    host": "hexlet.io",
    "  - timeout": "50",
    "  + timeout": "20",
    "  - follow": "false",
    "  - proxy": "123.234.53.22",
    "  + verbose": "true",
  }


def right_stylish():
    return generate_stylish.stulish(file)

