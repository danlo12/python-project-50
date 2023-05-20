import json
import yaml


def definition_form(file_path):
    extension = file_path[-4:]
    return (open(file_path)), extension


def format_definition(file_path):
    file, extension = definition_form(file_path)
    if extension == "json":
        return dict((json.load(file)).items())
    elif extension == "yaml" or extension == ".yml":
        return dict((yaml.safe_load(file)).items())
    else:
        raise ValueError('Unsupported format. '
                         'Next formats are supported: .json .yaml .yml')
