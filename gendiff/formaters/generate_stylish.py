def format_value(value, lvl):
    if value is None:
        return "null"
    elif isinstance(value, bool):
        return str(value).lower()
    elif isinstance(value, int) or isinstance(value, float):
        return str(value)
    elif isinstance(value, list):
        return walk_and_build_result(value, lvl + 4)
    else:
        return f"{value}"


def walk_and_build_result(content, lvl=2):
    final = []
    output = []
    for key in sorted(content, key=lambda k: k["name_key"]):
        not_updated = " " * lvl + "  " + key["name_key"] + ": "
        added = " " * lvl + "+ " + key["name_key"] + ": "
        removed = " " * lvl + "- " + key["name_key"] + ": "
        if key["type"] == "not updated":
            output.append(not_updated + format_value(key["value"], lvl))
        elif key["type"] == "updated":
            output.append(removed + format_value(key["old_value"], lvl))
            output.append(added + format_value(key["new_value"], lvl))
        elif key["type"] == "removed":
            output.append(removed + format_value(key["old_value"], lvl))
        elif key["type"] == "added":
            output.append(added + format_value(key["new_value"], lvl))
    final.append("{" + "\n" + "\n".join(output) + "\n" + (" " * (lvl - 2)) + "}")
    result = "\n".join(final)
    return result


def stylish(content):
    return walk_and_build_result(content)
