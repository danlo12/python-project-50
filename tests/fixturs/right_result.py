from gendiff import generate_diff

file = {
    '- follow': False,
    '  host': 'hexlet.io',
    '- proxy': '123.234.53.22',
    '- timeout': 50,
    '+ timeout': 20,
    '+ verbose': True}


def right_one():
    return generate_diff.mk_str(file)





def right_rec():
   return generate_diff.mk_str(result_rec)
