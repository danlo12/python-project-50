import json
import yaml


def load_and_select_formatter(file_path):
    extension = file_path[-4:]
    content = open(file_path)
    return select_formatter(content, extension)


def select_formatter(content, extension):
    if extension == "json":
        return dict((json.load(content)).items())
    if extension == "yaml" or extension == ".yml":
        return dict((yaml.safe_load(content)).items())
    raise ValueError('Unsupported format. '
                     'Next formats are supported: .json .yaml .yml')
