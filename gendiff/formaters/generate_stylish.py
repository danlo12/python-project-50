def format_value(value, lvl):
    if value is None:
        return "null"
    elif isinstance(value, bool):
        return str(value).lower()
    elif isinstance(value, int) or isinstance(value, float):
        return str(value)
    elif isinstance(value,list):
        return walk_and_build_result(value, lvl + 4)
    else:
        return f"{value}"


def walk_and_build_result(result,lvl=2):
    final = []
    output = []
    for key in sorted(result, key=lambda k: k["name_key"]):
        if key["type"] == "common_rec" or key["type"] == "common":
            output.append(" " * lvl + "  " + key["name_key"] + ": " + format_value(key["value"], lvl))
        elif key["type"] == "updated":
            output.append(" " * lvl + "- " + key["name_key"] + ": " + format_value(key["old_value"], lvl))
            output.append(" " * lvl + "+ " + key["name_key"] + ": " + format_value(key["new_value"], lvl))
        elif key["type"] == "removed_rec" or key["type"] == "removed":
            output.append(" " * lvl + "- " + key["name_key"] + ": " + format_value(key["old_value"], lvl))
        elif key["type"] == "added_rec" or key["type"] == "added":
            output.append(" " * lvl + "+ " + key["name_key"] + ": " + format_value(key["new_value"], lvl))
        elif key["type"] == "added":
            output.append(" " * lvl + "+ " + key["name_key"] + ": " + format_value(key["new_value"], lvl))
    final.append("{" + "\n" + "\n".join(output) + "\n" + (" " * (lvl - 2)) + "}")
    string_result = ""
    for string in "\n".join(final):
        string_result = string_result + string
    return string_result


def stylish(result):
    return walk_and_build_result(result)

