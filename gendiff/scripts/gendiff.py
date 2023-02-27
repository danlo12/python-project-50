#!/usr/bin/env python3
import argparse


def main():
    parser = argparse.ArgumentParser(description='Compares two configuration files and shows a difference.')
    parser.add_argument('first_file')
    parser.add_argument("second_file")
    parser.add_argument('-f','--format', dest='format', help='sum the integers (default: find the max)')
    args = parser.parse_args()
    return args.accumulate(args.integers)


if __name__ == '__main__':
    main()
