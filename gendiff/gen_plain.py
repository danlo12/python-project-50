

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


def format_value(value):
    if value is None:
        return "null"
    elif isinstance(value, bool):
        return str(value).lower()
    elif isinstance(value, int) or isinstance(value, float):
        return str(value)
    else:
        return f"'{value}'"


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


def plain(file1, file2, top_key=""):
    result = []
    for key in file2:
        if key in file1:
            if file1[key] == file2[key]:
                continue
            elif isinstance(file1[key], dict) and isinstance(file2[key], dict):
                result.append(plain(file1[key], file2[key], top_key + key + "."))
            else:
                if isinstance(file1[key], dict):
                    result.append(f"Property '{top_key}{key}' was updated. From [complex value] to {format_value(file2[key])}")
                elif isinstance(file2[key], dict):
                    result.append(f"Property '{top_key}{key}' was updated. From {format_value(file1[key])} to [complex value]")
                else:
                    result.append(f"Property '{top_key}{key}' was updated. From {format_value(file1[key])} to {format_value(file2[key])}")
        else:
            if isinstance(file2[key], dict):
                result.append(f"Property '{top_key}{key}' was added with value: [complex value]")
            else:
                result.append(f"Property '{top_key}{key}' was added with value: {format_value(file2[key])}")
    for key_removed in file1:
        if key_removed not in file2:
            result.append(f"Property '{top_key}{key_removed}' was removed")
    sorted_result = sorted(result, key=extract_key)
    result_string = "\n".join(sorted_result)
    return result_string
