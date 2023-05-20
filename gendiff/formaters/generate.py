def generate_key_lists(file1, file2,):
    common = list()
    n_common = list()
    for key1 in file1:
        if key1 in file2:
            common.append(key1)
        else:
            n_common.append(key1)
    for key2 in file2:
        if key2 in file1:
            continue
        else:
            n_common.append(key2)
    return common, n_common


def generate(file1, file2):
    result = list()
    common, not_common = generate_key_lists(file1, file2)[0], generate_key_lists(file1, file2)[1]
    for key_common in common:
        if type(file1[key_common]) is dict and type(file2[key_common]) is dict:
            result.append({"type": "common_rec", "name_key": key_common, "value": generate(file1[key_common], file2[key_common])})
        elif type(file1[key_common]) is dict and type(file2[key_common]) is not dict:
            result.append({"type": "updated1", "name_key": key_common, "new_value": file2[key_common], "old_value": generate(file1[key_common], file1[key_common])})
        elif type(file1[key_common]) is not dict and type(file2[key_common]) is dict:
            result.append({"type": "updated2", "name_key": key_common, "new_value": generate(file2[key_common], file2[key_common]), "old_value": file1[key_common]})
        elif file1[key_common] != file2[key_common]:
            result.append({"type": "updated3", "name_key": key_common, "new_value": file2[key_common], "old_value": file1[key_common]})
        else:
            result.append({"type": "common", "name_key": key_common, "value": file1[key_common]})
    for key_not_common in not_common:
        if key_not_common in file1:
            if type(file1[key_not_common]) is dict:
                result.append({"type": "removed_rec", "name_key": key_not_common, "old_value": generate(file1[key_not_common], file1[key_not_common])})
            else:
                result.append({"type": "removed", "name_key": key_not_common, "old_value": file1[key_not_common]})
        elif key_not_common in file2:
            if type(file2[key_not_common]) is dict:
                result.append({"type": "added_rec", "name_key": key_not_common, "new_value": generate(file2[key_not_common], file2[key_not_common])})
            else:
                result.append({"type": "added", "name_key": key_not_common, "new_value": file2[key_not_common]})
    return result
