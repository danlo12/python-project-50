def build_dicts_diff(content1, content2):
    result = list()
    common, not_common = list(set(content1) & set(content2)), list(set(content1) ^ set(content2))
    for key_common in common:
        if isinstance(content1[key_common], dict) and isinstance(content2[key_common], dict):
            result.append({"type": "common", "name_key": key_common, "value": build_dicts_diff(content1[key_common], content2[key_common])})
        elif isinstance(content1[key_common], dict) and isinstance(content2[key_common], dict) is False:
            result.append({"type": "updated", "name_key": key_common, "new_value": content2[key_common], "old_value": build_dicts_diff(content1[key_common], content1[key_common])})
        elif isinstance(content1[key_common], dict) is False and isinstance(content2[key_common], dict):
            result.append({"type": "updated", "name_key": key_common, "new_value": build_dicts_diff(content2[key_common], content2[key_common]), "old_value": content1[key_common]})
        elif content1[key_common] != content2[key_common]:
            result.append({"type": "updated", "name_key": key_common, "new_value": content2[key_common], "old_value": content1[key_common]})
        else:
            result.append({"type": "common", "name_key": key_common, "value": content1[key_common]})
    for key_not_common in not_common:
        if key_not_common in content1:
            if isinstance(content1[key_not_common], dict):
                result.append({"type": "removed", "name_key": key_not_common, "old_value": build_dicts_diff(content1[key_not_common], content1[key_not_common])})
            else:
                result.append({"type": "removed", "name_key": key_not_common, "old_value": content1[key_not_common]})
        elif key_not_common in content2:
            if type(content2[key_not_common]) is dict:
                result.append({"type": "added", "name_key": key_not_common, "new_value": build_dicts_diff(content2[key_not_common], content2[key_not_common])})
            else:
                result.append({"type": "added", "name_key": key_not_common, "new_value": content2[key_not_common]})
    return result
