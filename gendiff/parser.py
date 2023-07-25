import json
import yaml
import os


def get_content(file_path):
    extension = os.path.splitext(file_path)
    with open(file_path) as content:
        return parse_formatter(content, extension[1])


def parse_formatter(content, extension):
    if extension == ".json":
        return json.load(content)
    if extension == ".yaml" or extension == ".yml":
        return yaml.safe_load(content)
    raise ValueError('Unsupported format. '
                     'Next formats are supported: .json .yaml .yml')
