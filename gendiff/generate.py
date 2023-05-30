def generate(file1, file2):
    result = list()
    common, not_common = list(set(file1) & set(file2)), list(set(file1) ^ set(file2))
    for key_common in common:
        if type(file1[key_common]) is dict and type(file2[key_common]) is dict:
            result.append({"type": "common_rec", "name_key": key_common, "value": generate(file1[key_common], file2[key_common])})
        elif type(file1[key_common]) is dict and type(file2[key_common]) is not dict:
            result.append({"type": "updated", "name_key": key_common, "new_value": file2[key_common], "old_value": generate(file1[key_common], file1[key_common])})
        elif type(file1[key_common]) is not dict and type(file2[key_common]) is dict:
            result.append({"type": "updated", "name_key": key_common, "new_value": generate(file2[key_common], file2[key_common]), "old_value": file1[key_common]})
        elif file1[key_common] != file2[key_common]:
            result.append({"type": "updated", "name_key": key_common, "new_value": file2[key_common], "old_value": file1[key_common]})
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
    print(result)
    return result
