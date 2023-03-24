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
    print(generate_diff.mk_str(file))
    return generate_diff.mk_str(file)
