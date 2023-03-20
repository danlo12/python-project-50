from gendiff import generate_diff

file = {
    '- follow': False,
    '  host': 'hexlet.io',
    '- proxy': '123.234.53.22',
    '- timeout': 50,
    '+ timeout': 20,
    '+ verbose': True}


def right():
    return generate_diff.mk_str(file)
