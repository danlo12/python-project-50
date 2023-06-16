def build_dicts_diff(content1, content2):
    result = []
    keys = set(content1.keys()).union(content2.keys())
    for key in keys:
        if key in content1 and key in content2:
            if isinstance(content1[key], dict) and isinstance(content2[key], dict):
                result.append(
                    {"type": "not updated", "name_key": key, "value": build_dicts_diff(content1[key], content2[key])})
            elif isinstance(content1[key], dict) and not isinstance(content2[key], dict):
                result.append({"type": "updated", "name_key": key, "new_value": content2[key],
                               "old_value": build_dicts_diff(content1[key], content1[key])})
            elif not isinstance(content1[key], dict) and isinstance(content2[key], dict):
                result.append(
                    {"type": "updated", "name_key": key, "new_value": build_dicts_diff(content2[key], content2[key]),
                     "old_value": content1[key]})
            elif content1[key] != content2[key]:
                result.append(
                    {"type": "updated", "name_key": key, "new_value": content2[key], "old_value": content1[key]})
            else:
                result.append({"type": "not updated", "name_key": key, "value": content1[key]})
        elif key in content1:
            if isinstance(content1[key], dict):
                result.append(
                    {"type": "removed", "name_key": key, "old_value": build_dicts_diff(content1[key], content1[key])})
            else:
                result.append({"type": "removed", "name_key": key, "old_value": content1[key]})
        else:
            if isinstance(content2[key], dict):
                result.append(
                    {"type": "added", "name_key": key, "new_value": build_dicts_diff(content2[key], content2[key])})
            else:
                result.append({"type": "added", "name_key": key, "new_value": content2[key]})
    return result
