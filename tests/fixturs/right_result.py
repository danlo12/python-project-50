from gendiff import generate_diff

def right():
    return generate_diff.mk_str({'- follow': False, '  host': 'hexlet.io', '- proxy': '123.234.53.22', '- timeout': 50, '+ timeout': 20, '+ verbose': True})
