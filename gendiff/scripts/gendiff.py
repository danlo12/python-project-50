#!/usr/bin/env python3
from gendiff import cli
from gendiff.gendiff import generate_diff


def main():
    print(generate_diff(cli.parse_args()[0], cli.parse_args()[1], cli.parse_args()[2]))


if __name__ == '__main__':
    main()
