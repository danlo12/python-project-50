from gendiff.parser import definition_form


def stulish(result, lvl=2):
    final = "{"
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


def generate_dict(file1, file2):
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
    common, n_common = generate_dict(file1, file2)[0], generate_dict(file1, file2)[1]
    for key_all in common:
        if type(file1[key_all]) is dict and type(file2[key_all]) is dict:
            result[(" " * lvl) + "  " + key_all] = stulish(generate(file1[key_all], file2[key_all], lvl + 4), lvl + 2)
        elif type(file1[key_all]) is dict and type(file2[key_all]) is not dict:
            result[(" " * lvl) + "- " + key_all] = stulish(generate(file1[key_all], file1[key_all], lvl + 4), lvl + 2)
            result[(" " * lvl) + "+ " + key_all] = file2[key_all]
        elif type(file1[key_all]) is not dict and type(file2[key_all]) is dict:
            result[(" " * lvl) + "- " + key_all] = file1[key_all]
            result[(" " * lvl) + "+ " + key_all] = stulish(generate(file2[key_all], file2[key_all], lvl + 4), lvl + 2)
        elif file1[key_all] != file2[key_all]:
            result[(" " * lvl) + "- " + key_all] = file1[key_all]
            result[(" " * lvl) + "+ " + key_all] = file2[key_all]
        else:
            result[(" " * lvl) + "  " + key_all] = file1[key_all]
    timer = 0
    for file_value in (file1, file2):
        timer += 1
        for key in n_common:
            if key in file_value:
                if type(file_value[key]) is dict and timer == 1:
                    result[(" " * lvl) + "- " + key] = stulish(generate(file_value[key], file_value[key], lvl + 4), lvl + 2)
                elif type(file_value[key]) is dict and timer == 2:
                    result[(" " * lvl) + "+ " + key] = stulish(generate(file_value[key], file_value[key], lvl + 4), lvl + 2)
                else:
                    if timer == 1:
                        result[(" " * lvl) + "- " + key] = file_value[key]
                    else:
                        result[(" " * lvl) + "+ " + key] = file_value[key]
    return result


def return_result(file_path1, file_path2, formater="stylish"):
    file1 = definition_form(file_path1)
    file2 = definition_form(file_path2)
    if formater == "stylish":
        return stulish(generate(file1, file2))
