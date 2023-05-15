from gendiff.parser import definition_form
from gendiff.generate_stylish import generate, stulish
from gendiff.gen_plain import plain
from gendiff.generate_json import json_s


def generate_diff(file_path1, file_path2, formater="stylish"):
    file1 = definition_form(file_path1)
    file2 = definition_form(file_path2)
    formater = formater.lower()
    if formater == "stylish":
        return stulish(generate(file1, file2))
    if formater == "plain":
        return plain(file1, file2)
    if formater == "json":
        return json_s(generate(file1, file2))
