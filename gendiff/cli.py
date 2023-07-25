import argparse


def parse_args():
    desctipt = 'Compares two configuration files and shows a difference.'
    parser = argparse.ArgumentParser(description=desctipt)
    parser.add_argument('first_file')
    parser.add_argument("second_file")
    f_help = 'set format of output'
    parser.add_argument('-f', '--format', dest='format',
                        help=f_help, default="STYLISH")
    return parser.parse_args()
