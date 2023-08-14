

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


def build_line(name, key):
    if key["type"] == "nested":
        return (plain(key
                      ["value"], name + key["name_key"] + "."))

    elif key["type"] == "updated":
        return (f"Property '{name}{key['name_key']}"
                f"' was updated. From "
                f"{to_str(key['old_value'])} " f"to {to_str(key['new_value'])}")
    elif key["type"] == "removed":
        return (f"Property "
                f"'{name}{key['name_key']}' was removed")
    elif key["type"] == "added":
        return (f"Property '{name}{key['name_key']}' "
                f"was added with value: {to_str(key['new_value'])}")


def plain(content, prefix_path=""):
    output = []
    for key in content:
        result = build_line(prefix_path, key)
        if result is not None:
            output.append(build_line(prefix_path, key))
        else:
            continue
    return "\n".join(output)
