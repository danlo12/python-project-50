

def plain2(file1, file2, top_key=""):
    result = ""
    for key in file2:
        if key in file1:
            if file1[key] == file2[key]:
                continue
            elif type(file1[key]) is dict and type(file2[key]) is dict:
                result += (plain(file1[key], file2[key], top_key + key + "."))
            else:
                if type(file1[key]) is dict:
                    result += "\nProperty " + top_key + key + " was updated. From " + \
                              "[complex value]" + " to " + str(file2[key])
                elif type(file2[key]) is dict:
                    result += "\nProperty " + top_key + key + " was updated. From " + \
                              str(file1[key]) + " to " + "[complex value]"
                else:
                    result += "\nProperty " + top_key + key + " was updated. From " + \
                              str(file1[key]) + " to " + str(file2[key])
        else:
            if type(file2[key]) is dict:
                result += "\nProperty " + top_key + key + " was added with value: [complex value]"
            else:
                result += "\nProperty " + top_key + key + " was added with value:  " + str(file2[key])
    for key_removed in file1:
        if key_removed not in file2:
            result += "\nProperty " + top_key + key_removed + " was removed"
    return result


def extract_key(s):
    parts = s.split("Property ")
    if len(parts) > 1:
        return parts[1]
    else:
        return s


def plain(file1, file2, top_key=""):
    result = list()
    for key in file2:
        if key in file1:
            if file1[key] == file2[key]:
                continue
            elif type(file1[key]) is dict and type(file2[key]) is dict:
                result.append(plain(file1[key], file2[key], top_key + key + "."))
            else:
                if type(file1[key]) is dict:
                    x = str(file2[key])
                    result.append(f'\nProperty {top_key}{key} was updated. From [complex value] to {x}')
                elif type(file2[key]) is dict:
                    result.append(f'\nProperty + {top_key}{key} was updated. From {str(file1[key])} to [complex value]')
                else:
                    result.append(f'\nProperty + {top_key} + {key}  was updated. From " + {str(file1[key])} + " to " + {str(file2[key])}')
        else:
            if type(file2[key]) is dict:
                result.append(f'\nProperty {top_key}{key} was added with value: [complex value]')
            else:
                result.append(f'\nProperty {top_key}{key} was added with value: {str(file2[key])}')
    for key_removed in file1:
        if key_removed not in file2:
            result.append(f'\nProperty {top_key}{key_removed} was removed')
    list_string = str()
    for string in result:
        list_string += string
    list_string = list_string.split(sep="\n")
    list_string.pop(0)
    sorted_string = sorted(list_string, key=extract_key)
    result_string = ""
    for string in sorted_string:
        result_string += string + "\n"
    return result_string


def find_int(list_r):
    result = list()
    for string in list_r:
        for intr in string:
            if intr.isdigit() is True:
               index = string.index(intr)
               if string[index].isdigit() is True:
                   result.append(string)
               else:
                   continue
        for x in result:
            print(x)
