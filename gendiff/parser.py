import json
import yaml
import os


def get_content(file_path):
    _, extension = os.path.splitext(file_path)
    with open(file_path) as content:
        return parse_content(content, extension[1:])


def content_check(content, extension):
    if extension == "json":
        return json.load(content)
    if extension in ("yml", "yaml"):
        return yaml.safe_load(content)
    raise ValueError('Unsupported format. '
                     'Next formats are supported: .json .yaml .yml')


def parse_content(content, extension):
    return content_check(content, extension)
