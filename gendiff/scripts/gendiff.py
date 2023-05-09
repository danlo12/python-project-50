#!/usr/bin/env python3
import argparse
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
def main():
    desctipt = 'Compares two configuration files and shows a difference.'
    parser = argparse.ArgumentParser(description=desctipt)
    parser.add_argument('first_file')
    parser.add_argument("second_file")
    f_help = 'set format of output'
    parser.add_argument('-f', '--format', dest='format', help=f_help, default="STYLISH")
    args = parser.parse_args()
    return generate_diff(args.first_file, args.second_file, args.format)


if __name__ == '__main__':
    main()
