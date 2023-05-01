
def json_s(result, lvl=2):
    final = '{'
    for str_result in result:
        if result[str_result] is True or result[str_result] is False:
            result[str_result] = str(result[str_result]).lower()
        elif result[str_result] is None:
            result[str_result] = "null"
        else:
            result[str_result] = str(result[str_result])
        if len(final) == 1:
            final = final + "\n" + '"' + str(str_result) + '"' + ': ' + result[str_result]
        elif len(final) != 1:
            final = final + ',' + "\n" + '"' + str(str_result) + '"' + ': ' + result[str_result]
    final = final + "\n" + (" " * lvl) + "}"
    return final
