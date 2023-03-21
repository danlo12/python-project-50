def mk_str(result):
    final = "{"
    for str_result in result:
        if result[str_result] is True or result[str_result] is False:
            result[str_result] = str(result[str_result]).lower()
        else:
            result[str_result] = str(result[str_result])
        final = final + "\n" + str(str_result) + ': ' + result[str_result]
    final = final + "\n}"
    return final


def recdif(file1, file2, lvl=2):
    result = dict()
    for key1 in file1:
        if type(file1) is str:
           return result
        if type(file1[key1]) is dict:
            if key1 in file2 and isinstance(file2[key1], dict):
                result[(" " * lvl) + "  " + key1] = mk_str(recdif(file1[key1], file2[key1], lvl * 2))
            else:
                result[(" " * lvl) + "- " + key1] = mk_str(recdif(file1[key1],file1[key1],lvl * 2))
        else:
            if key1 in file2:
                if file1[key1] == file2[key1]:
                    result[(" " * lvl) + "  " + key1] = file1[key1]
                else:
                    result[(" " * lvl) + "- " + key1] = file1[key1]
                    result[(" " * lvl) + "+ " + key1] = file2[key1]
            else:
                result[(" " * lvl) + "- " + key1] = file1[key1]
    for key2 in file2:
        if type(file2) is str:
            return result
        if type(file2[key2]) is dict:
            if key2 in file1 and isinstance(file1[key2], dict):
                continue
            else:
                result[(" " * lvl) + "+ " + key2] = mk_str(recdif(file2[key2], file2[key2], lvl * 2))
        else:
            for key2 in file2:
                if key2 in file1:
                    continue
                else:
                    result[(" " * lvl) + "+ " + key2] = file2[key2]
    return result
