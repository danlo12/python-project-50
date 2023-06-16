from gendiff.parser import load_and_select_formatter
from gendiff.formaters import choice_formater
from gendiff.generate import build_dicts_diff


def generate_diff(file_path1, file_path2, formater="stylish"):
    file1 = load_and_select_formatter(file_path1)
    file2 = load_and_select_formatter(file_path2)
    content = build_dicts_diff(file1, file2)
    return choice_formater.apply_formatter(content, formater)
