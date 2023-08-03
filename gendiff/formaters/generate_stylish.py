def format_value(value, lvl):
    if value is None:
        return "null"
    if isinstance(value, bool):
        return str(value).lower()
    if isinstance(value, int) or isinstance(value, float):
        return str(value)
    if isinstance(value, list):
        return walk_and_build_result(value, lvl + 4)
    return f"{value}"


def walk_and_build_result(content, lvl=2):
    final = []
    output = []
    for key in content:
        if key["type"] == "not updated" or key["type"] == "nested":
            not_updated = " " * lvl + "  " + key["name_key"] + ": "
            output.append(not_updated + format_value(key["value"], lvl))
        elif key["type"] == "updated":
            added = " " * lvl + "+ " + key["name_key"] + ": "
            removed = " " * lvl + "- " + key["name_key"] + ": "
            output.append(removed + format_value(key["old_value"], lvl))
            output.append(added + format_value(key["new_value"], lvl))
        elif key["type"] == "removed":
            removed = " " * lvl + "- " + key["name_key"] + ": "
            output.append(removed + format_value(key["old_value"], lvl))
        elif key["type"] == "added":
            added = " " * lvl + "+ " + key["name_key"] + ": "
            output.append(added + format_value(key["new_value"], lvl))
    final.append(
        "{" + "\n" + "\n".join(output) + "\n" + (" " * (lvl - 2)) + "}")
    result = "\n".join(final)
    return result


def stylish(content):
    return walk_and_build_result(content)
