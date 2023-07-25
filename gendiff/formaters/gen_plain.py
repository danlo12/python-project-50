

def to_str(value):
    if value is None:
        return "null"
    if isinstance(value, bool):
        return str(value).lower()
    if isinstance(value, int) or isinstance(value, float):
        return str(value)
    if isinstance(value, list):
        return "[complex value]"
    return f"'{value}'"


def plain(content, name=""):
    output = []
    for key in content:
        if key["type"] == "not updated":
            if isinstance(key["value"], list):
                output.append(plain(key["value"], name + key["name_key"] + "."))
            else:
                continue
        elif key["type"] == "updated":
            output.append(f"Property '{name}{key['name_key']}"
                          f"' was updated. From {to_str(key['old_value'])} "
                          f"to {to_str(key['new_value'])}")
        elif key["type"] == "removed":
            output.append(f"Property '{name}{key['name_key']}' was removed")
        elif key["type"] == "added":
            output.append(f"Property '{name}{key['name_key']}' "
                          f"was added with value: {to_str(key['new_value'])}")
    return "\n".join(output)
