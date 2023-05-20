def extract_key(s):
    parts = s.split("Property ")
    if len(parts) > 1:
        return parts[1]
    else:
        return s


def format_value(value):
    if value is None:
        return "null"
    elif isinstance(value, bool):
        return str(value).lower()
    elif isinstance(value, int) or isinstance(value, float):
        return str(value)
    else:
        return f"'{value}'"


def plain(result, name=""):
    output = []
    for key in sorted(result, key=lambda k: k["name_key"]):
        if key["type"] == "common_rec":
            output.append(plain(key["value"], name + key["name_key"] + "."))
        elif key["type"] == "common":
            continue
        elif key["type"] == "updated1":
            output.append(f"Property '{name}{key['name_key']}' was updated. From [complex value] to {format_value(key['new_value'])}")
        elif key["type"] == "updated2":
            output.append(f"Property '{name}{key['name_key']}' was updated. From {format_value(key['old_value'])} to [complex value]")
        elif key["type"] == "updated3":
            output.append(f"Property '{name}{key['name_key']}' was updated. From {format_value(key['old_value'])} to {format_value(key['new_value'])}")
        elif key["type"] == "removed_rec":
            output.append(f"Property '{name}{key['name_key']}' was removed")
        elif key["type"] == "removed":
            output.append(f"Property '{name}{key['name_key']}' was removed")
        elif key["type"] == "added_rec":
            output.append(f"Property '{name}{key['name_key']}' was added with value: [complex value]")
        elif key["type"] == "added":
            output.append(f"Property '{name}{key['name_key']}' was added with value: {format_value(key['new_value'])}")
    string_result = ""
    for string in "\n".join(output):
        string_result = string_result + string
    return string_result
