import json


def format_value(value):
    if value is None:
        return "null"
    elif isinstance(value, bool):
        return str(value).lower()
    elif isinstance(value, int) or isinstance(value, float):
        return str(value)
    else:
        return f"{value}"


def json_f(result, lvl=2):
    final = []
    output = dict()
    for key in sorted(result, key=lambda k: k["name_key"]):
        if key["type"] == "common_rec":
            output[" " * lvl + "  " + key["name_key"]] = json_f(key["value"], lvl + 4)
        elif key["type"] == "common":
            output[" " * lvl + "  " + key["name_key"]] = format_value(key["value"])
        elif key["type"] == "updated1":
            output[" " * lvl + "- " + key["name_key"]] = json_f(key["old_value"], lvl + 4)
            output[" " * lvl + "+ " + key["name_key"]] = format_value(key["new_value"])
        elif key["type"] == "updated2":
            output[" " * lvl + "- " + key["name_key"]] = format_value(key["old_value"])
            output[" " * lvl + "+ " + key["name_key"]] = json_f(key["new_value"], lvl + 4)
        elif key["type"] == "updated3":
            output[" " * lvl + "- " + key["name_key"]] = format_value(key["old_value"])
            output[" " * lvl + "+ " + key["name_key"]] = format_value(key["new_value"])
        elif key["type"] == "removed_rec":
            output[" " * lvl+ "- " + key["name_key"]] = json_f(key["old_value"], lvl + 4)
        elif key["type"] == "removed":
            output[" " * lvl + "- " + key["name_key"]] = format_value(key["old_value"])
        elif key["type"] == "added_rec":
            output[" " * lvl + "+ " + key["name_key"]] = json_f(key["new_value"], lvl + 4)
        elif key["type"] == "added":
            output[" " * lvl + "+ " + key["name_key"]] = format_value(key["new_value"])
    final.append("{" + "\n" + "\n".join(output) + "\n" + (" " * (lvl - 2)) + "}")
    return json.dumps(output)
