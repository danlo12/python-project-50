from gendiff.formaters.generate_stylish import stylish
from gendiff.formaters.gen_plain import plain
from gendiff.formaters.generate_json import json_f


def definition_formater(content, formater):
    formater = formater.lower()
    if formater == "stylish":
        return stylish(content)
    if formater == "plain":
        return plain(content)
    if formater == "json":
        return json_f(content)
    else:
        raise ValueError('Unsupported formater. '
                         'Next formaters are supported: stylish, plain, json')