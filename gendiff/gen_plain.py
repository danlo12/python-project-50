

def plain(file1, file2, top_key=""):
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
