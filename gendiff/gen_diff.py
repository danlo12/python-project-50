from gendiff.parser import definition_form
from gendiff.generate_stylish import generate, stulish
from gendiff.gen_plain import plain
from gendiff.generate_json import json_s


def generate_diff(file_path1, file_path2, formater="STYLISH"):
    file1 = definition_form(file_path1)
    file2 = definition_form(file_path2)
    if formater == "STYLISH":
        return stulish(generate(file1, file2))
    if formater == "PLAIN":
        return plain(file1, file2)
    if formater == "JSON":
        return json_s(generate(file1, file2))

__all__ = ["generate_diff"]