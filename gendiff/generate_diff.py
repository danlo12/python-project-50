from gendiff.parser import definition_form


def mk_str(result, lvl=2):
    final = "{"
    for str_result in result:
        if result[str_result] is True or result[str_result] is False:
            result[str_result] = str(result[str_result]).lower()
        if result[str_result] is None:
            result[str_result] = "null"
        else:
            result[str_result] = str(result[str_result])
        final = final + "\n" + str(str_result) + ': ' + result[str_result]
    final = final + "\n" + (" " * lvl) + "}"
    return final


def generate(file1, file2, lvl=2):
    result = dict()
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
    for key_all in common:
        if type(file1[key_all]) is dict and type(file2[key_all]) is dict:
            result[(" " * lvl) + "  " + key_all] = mk_str(generate(file1[key_all], file2[key_all], lvl + 4), lvl + 2)
        elif type(file1[key_all]) is dict and type(file2[key_all]) is not dict:
            result[(" " * lvl) + "- " + key_all] = mk_str(generate(file1[key_all], file1[key_all], lvl + 4), lvl + 2)
            result[(" " * lvl) + "+ " + key_all] = file2[key_all]
        elif type(file1[key_all]) is not dict and type(file2[key_all]) is dict:
            result[(" " * lvl) + "- " + key_all] = file1[key_all]
            result[(" " * lvl) + "+ " + key_all] = mk_str(generate(file2[key_all], file2[key_all], lvl + 4), lvl + 2)
        elif file1[key_all] != file2[key_all]:
            result[(" " * lvl) + "- " + key_all] = file1[key_all]
            result[(" " * lvl) + "+ " + key_all] = file2[key_all]
        else:
            result[(" " * lvl) + "  " + key_all] = file1[key_all]
    for key_nall in n_common:
        if key_nall in file1:
            if type(file1[key_nall]) is dict:
                result[(" " * lvl) + "- " + key_nall] = mk_str(generate(file1[key_nall],
                                                                        file1[key_nall], lvl + 4), lvl + 2)
            else:
                result[(" " * lvl) + "- " + key_nall] = file1[key_nall]
        elif key_nall in file2:
            if type(file2[key_nall]) is dict:
                result[(" " * lvl) + "+ " + key_nall] = mk_str(generate(file2[key_nall],
                                                                        file2[key_nall], lvl + 4), lvl + 2)
            else:
                result[(" " * lvl) + "+ " + key_nall] = file2[key_nall]
    return result


def return_result(file_path1, file_path2):
    file1 = definition_form(file_path1)
    file2 = definition_form(file_path2)
    return mk_str(generate(file1, file2))
