import json


def json_f(result):
    result = sorted(result, key=lambda x: x["name_key"])
    result = json.dumps(result)
    return result
