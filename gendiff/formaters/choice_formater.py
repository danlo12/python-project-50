from gendiff.formaters.generate_stylish import stulish
from gendiff.formaters.gen_plain import plain
from gendiff.formaters.generate_json import json_f
from gendiff.formaters.generate import generate


def definition_formater(file1, file2, formater):
    formater = formater.lower()
    if formater == "stylish":
        return stulish(generate(file1, file2))
    if formater == "plain":
        return plain(generate(file1, file2))
    if formater == "json":
        return json_f(generate(file1, file2))
