import json


def json_s(result):
    for arg in result:
        if result[arg] is True or result[arg] is False:
            result[arg] = str(result[arg]).lower()
    return json.dumps(result)
