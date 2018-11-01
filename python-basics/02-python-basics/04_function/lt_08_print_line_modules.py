def print_line(char, times):
    """
    打印单行分隔线
    :param char: 字符
    :param times: 重复次数
    :return:
    """
    print(char * times)


def print_lines(char, times, rows):
    """
    打印多行分隔线
    :param char: 字符
    :param times: 每行字符数
    :param rows: 行数
    :return:
    """
    row = 0

    while row < rows:
        print_line(char, times)
        row += 1


name = "print line module"
