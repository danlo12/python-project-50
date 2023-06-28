import json
import yaml
import os


def load_and_parse_formatter(file_path):
    extension = os.path.splitext(file_path)[1]
    content = open(file_path)
    return parse_formatter(content, extension)


def parse_formatter(content, extension):
    if extension == ".json":
        return dict((json.load(content)).items())
    if extension == ".yaml" or extension == ".yml":
        return dict((yaml.safe_load(content)).items())
    raise ValueError('Unsupported format. '
                     'Next formats are supported: .json .yaml .yml')
