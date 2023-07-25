def operation_for_add(content, key):
    if isinstance(content, dict):
        return {"type": "added", "name_key": key,
                "new_value": build_dicts_diff(content, content)}
    else:
        return {"type": "added", "name_key": key, "new_value": content}


def operation_for_delete(content, key):
    if isinstance(content, dict):
        return {"type": "removed", "name_key": key,
                "old_value": build_dicts_diff(content, content)}
    else:
        return {"type": "removed", "name_key": key, "old_value": content}


def build_dicts_diff(content1, content2):
    keys = content1.keys() | content2.keys()
    added = content2.keys() - content1.keys()
    deleted = content1.keys() - content2.keys()
    result = []
    for key in keys:
        if key in added:
            result.append(operation_for_add(content2[key], key))
        if key in deleted:
            result.append(operation_for_delete(content1[key], key))
        if key in content1 and key in content2:
            if isinstance(content1[key], dict) and \
                    isinstance(content2[key], dict):
                result.append({"type": "not updated",
                               "name_key": key,
                               "value": build_dicts_diff(content1[key],
                                                         content2[key])})
                continue
            if isinstance(content1[key], dict):
                result.append({"type": "updated", "name_key": key,
                               "new_value": content2[key],
                               "old_value": build_dicts_diff(content1[key],
                                                             content1[key])})
                continue
            if isinstance(content2[key], dict):
                result.append({"type": "updated", "name_key": key,
                               "new_value": build_dicts_diff(content2[key],
                                                             content2[key]),
                               "old_value": content1[key]})
                continue
            if content1[key] != content2[key]:
                result.append(
                    {"type": "updated", "name_key": key,
                     "new_value": content2[key], "old_value": content1[key]})
                continue
            else:
                result.append({"type": "not updated",
                               "name_key": key, "value": content1[key]})
    return sorted(result, key=lambda k: k["name_key"])
