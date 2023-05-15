from gendiff import generate_stylish
file = {
    "    host": "hexlet.io",
    "  - timeout": "50",
    "  + timeout": "20",
    "  - proxy": "123.234.53.22",
    "  - follow": "false",
    "  + verbose": "true",
  }


def right_stylish():
    return generate_stylish.stulish(file)
