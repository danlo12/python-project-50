from gendiff.parser import definition_form
from gendiff.Gendiff import generate

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


def generate_diff(file1, file2,):
    file1 = file1
    result = dict()
    for key1 in file1:
        if key1 in file2:
            if file1[key1] == file2[key1]:
                result["  " + key1] = file1[key1]
            else:
                result["- " + key1] = file1[key1]
                result["+ " + key1] = file2[key1]
        else:
            result["- " + key1] = file1[key1]
    for key2 in file2:
        if key2 in file1:
            continue
        else:
            result["+ " + key2] = file2[key2]
    return result


def return_result(file_path1, file_path2):
    file1 = definition_form(file_path1)
    file2 = definition_form(file_path2)
    return mk_str(generate(file1, file2))
