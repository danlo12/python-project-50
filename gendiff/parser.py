import json
import yaml


def define_format(file_path):
    extension = file_path[-4:]
    content = open(file_path)
    return format_definition(content, extension)


def format_definition(content, extension):
    if extension == "json":
        return dict((json.load(content)).items())
    elif extension == "yaml" or extension == ".yml":
        return dict((yaml.safe_load(content)).items())
    else:
        raise ValueError('Unsupported format. '
                         'Next formats are supported: .json .yaml .yml')
