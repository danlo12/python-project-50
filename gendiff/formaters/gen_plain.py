

def to_str(value):
    if value is None:
        return "null"
    elif isinstance(value, bool):
        return str(value).lower()
    elif isinstance(value, int) or isinstance(value, float):
        return str(value)
    elif isinstance(value, list):
        return "[complex value]"
    else:
        return f"'{value}'"


def plain(result, name=""):
    output = []
    for key in sorted(result, key=lambda k: k["name_key"]):
        if key["type"] == "common":
            if isinstance(key["value"], list):
                output.append(plain(key["value"], name + key["name_key"] + "."))
            else:
                continue
        elif key["type"] == "updated":
            output.append(f"Property '{name}{key['name_key']}' was updated. From {to_str(key['old_value'])} to {to_str(key['new_value'])}")
        elif key["type"] == "removed" or key["type"] == "removed_rec":
            output.append(f"Property '{name}{key['name_key']}' was removed")
        elif key["type"] == "added" or key["type"] == "added_rec":
            output.append(f"Property '{name}{key['name_key']}' was added with value: {to_str(key['new_value'])}")
    string_result = ""
    for string in "\n".join(output):
        string_result = string_result + string
    return string_result
