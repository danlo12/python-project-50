def sorter(result, slvl):
    for key in result:
        if isinstance(result[key], dict):
            result = result.items()
            result = sorted(result, key=lambda x: x[0][slvl + 1][-1])
            result = dict(result)
            result[key] = sorter(result[key], slvl + 4)
        else:
            result = result.items()
            result = sorted(result, key=lambda x: x[0][slvl + 1][-1])
            result = dict(result)
    return result


def stulish(result, lvl=0, slvl=4):
    final = "{"
    for arg in result:
        if isinstance(result[arg], dict):
            result = result.items()
            result = sorted(sorted(result, key=lambda x: x[0][-1]), key=lambda y: y[0][slvl])
            result = dict(result)
            result[arg] = stulish(result[arg], lvl + 4, slvl + 4)
    for str_result in result:
        if result[str_result] is True or result[str_result] is False:
            result[str_result] = str(result[str_result]).lower()
        elif result[str_result] is None:
            result[str_result] = "null"
        else:
            result[str_result] = str(result[str_result])
        final = final + "\n" + str(str_result) + ': ' + result[str_result]
    final = final + "\n" + (" " * lvl) + "}"
    return final


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


def generate(file1, file2, lvl=2):
    result = dict()
    common, not_common = generate_key_lists(file1, file2)[0], generate_key_lists(file1, file2)[1]
    for key_common in common:
        new_key1 = (" " * lvl) + "- " + key_common
        new_key2 = (" " * lvl) + "+ " + key_common
        new_key_all = (" " * lvl) + "  " + key_common
        if type(file1[key_common]) is dict and type(file2[key_common]) is dict:
            result[new_key_all] = generate(file1[key_common], file2[key_common], lvl + 4)
        elif type(file1[key_common]) is dict and type(file2[key_common]) is not dict:
            result[new_key1] = generate(file1[key_common], file1[key_common], lvl + 4)
            result[new_key2] = file2[key_common]
        elif type(file1[key_common]) is not dict and type(file2[key_common]) is dict:
            result[new_key1] = file1[key_common]
            result[new_key2] = generate(file2[key_common], file2[key_common], lvl + 4)
        elif file1[key_common] != file2[key_common]:
            result[new_key1] = file1[key_common]
            result[new_key2] = file2[key_common]
        else:
            result[new_key_all] = file1[key_common]
    for key_not_common in not_common:
        if key_not_common in file1:
            new_key1 = (" " * lvl) + "- " + key_not_common
            if type(file1[key_not_common]) is dict:
                result[new_key1] = generate(file1[key_not_common], file1[key_not_common], lvl + 4)
            else:
                result[new_key1] = file1[key_not_common]
        elif key_not_common in file2:
            new_key2 = (" " * lvl) + "+ " + key_not_common
            if type(file2[key_not_common]) is dict:
                result[new_key2] = generate(file2[key_not_common], file2[key_not_common], lvl + 4)
            else:
                result[new_key2] = file2[key_not_common]
    return result
