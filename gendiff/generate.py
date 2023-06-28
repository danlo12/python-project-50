def operation_for_add(content, key):
    if isinstance(content, dict):
        return {"type": "added", "name_key": key, "new_value": build_dicts_diff(content, content)}
    else:
        return {"type": "added", "name_key": key, "new_value": content}


def operation_for_delete(content, key):
    if isinstance(content, dict):
        return {"type": "removed", "name_key": key, "old_value": build_dicts_diff(content, content)}
    else:
        return {"type": "removed", "name_key": key, "old_value": content}


def nested_call_for_build_inner_elements(content1, content2, key):
    if isinstance(content1, dict) and isinstance(content2, dict):
        return {"type": "not updated", "name_key": key, "value": build_dicts_diff(content1, content2)}
    if isinstance(content1, dict):
        return {"type": "updated", "name_key": key, "new_value": content2,
                "old_value": build_dicts_diff(content1, content1)}
    if isinstance(content2, dict):
        return {"type": "updated", "name_key": key, "new_value": build_dicts_diff(content2, content2),
                "old_value": content1}
    if content1 != content2:
        return {"type": "updated", "name_key": key, "new_value": content2, "old_value": content1}
    else:
        return {"type": "not updated", "name_key": key, "value": content1}


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
            result.append(nested_call_for_build_inner_elements(content1[key], content2[key], key))
    return sorted(result, key=lambda k: k["name_key"])
