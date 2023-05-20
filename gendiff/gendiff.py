from gendiff.parser import format_definition
from gendiff.formaters import choice_formater


def generate_diff(file_path1, file_path2, formater="stylish"):
    file1 = format_definition(file_path1)
    file2 = format_definition(file_path2)
    return choice_formater.definition_formater(file1, file2, formater)
