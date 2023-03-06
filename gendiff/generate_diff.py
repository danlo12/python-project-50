import json


def generate_diff(file_path1, file_path2):
    file1 = dict(sorted((json.load(open(file_path1))).items()))
    file2 = dict(sorted((json.load(open(file_path2))).items()))
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
    final = "\n{"
    for str_result in result:
        if result[str_result] == True or result[str_result] == False:
            result[str_result] = str(result[str_result]).lower()
        else:
            result[str_result] = str(result[str_result])
        final = final + "\n" + str(str_result) + ': ' + result[str_result]
    final = final + "\n}"
    return final

