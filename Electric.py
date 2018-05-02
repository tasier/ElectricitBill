# -*- coding: UTF-8 -*-

from sys import argv


def count_statistics(last_month_number_filename, current_month_number_filename, current_fee_filename):
    """
    统计每个房间用电度数，总用电度数，每个房间需缴纳的费用
    :param last_month_number_filename:
    :param current_month_number_filename:
    :param current_fee_filename:
    :return:
    """
    room_number, total_number = count_number_statistics(last_month_number_filename, current_month_number_filename)

    total_fee = read_current_month_total_fee(current_fee_filename)

    room_fee = count_fee_statistics(room_number, total_number, total_fee)
    print_line_seperate_symbol()
    print_each_room_fee(room_fee, total_fee, room_number, total_number)


def count_fee_statistics(room_number, total_number, total_fee):
    """
    统计每个房间需缴纳的费用
    :param room_number:
    :param total_number:
    :param total_fee:
    :return:
    """
    result = {}

    # 房客数量(去除虚拟的公共房客)
    number_of_room = len(room_number) - 1

    for key in room_number:
        if cmp(key, '0') == 0:
            continue
        fee = (room_number[key] + room_number['0']/float(number_of_room))/total_number * total_fee
        #四舍五入取两位
        result[key] = round(fee, 2)

    return result


def count_number_statistics(last_month_number_filename, current_month_number_filename):
    """
    统计每个房间的用电量，以及总用电量
    :param last_month_number_filename:
    :param current_month_number_filename:
    :return:
    """
    last_room_number, current_room_number = \
        read_past_two_months_bill(last_month_number_filename, current_month_number_filename)

    # 统计每个房间的用电情况
    result_room_number = cout_each_room_number(last_room_number, current_room_number)
    print_each_room_number(last_room_number, current_room_number, result_room_number)

    print_line_seperate_symbol()

    # 统计所有的用电度数
    result_total_number = count_total_number(result_room_number)
    print_total_number(result_room_number, result_total_number)

    return result_room_number, result_total_number


def read_past_two_months_bill(last_month_number_filename, current_month_number_filename):
    """
    读取上个月和这个月的用电度数，返回房间号->度数dict
    :param last_month_number_filename:
    :param current_month_number_filename:
    :return: tuple
    """
    last_month_room_number = count_room_number_kv(open(last_month_number_filename, 'r').readlines())
    current_month_room_number = count_room_number_kv(open(current_month_number_filename, 'r').readlines())

    return last_month_room_number, current_month_room_number


def count_room_number_kv(content):
    """
    解析文件内容，返回csv文件对应的kv
    :param content:
    :return: dict
    """
    result = {}

    for line in content:
        line = line.strip()
        kv_list = line.split(',')
        result[kv_list[0]] = int(kv_list[1])

    return result


def read_current_month_total_fee(current_month_total_fee_filename):
    """
    获取当月电费的金额
    :param current_month_total_fee_filename:
    :return:
    """
    line = open(current_month_total_fee_filename).read()
    return float(line)


def cout_each_room_number(last_month_number, current_month_number):
    """
    计算每个房间用电度数情况
    :param last_month_number:
    :param current_month_number:
    :return:
    """
    result = {}

    for key in current_month_number:
        result[key] = current_month_number[key] - last_month_number[key]

    return result


def count_total_number(result_room_number):
    """
    计算当月使用的电费度数
    :param result_room_number:
    :return:
    """
    result = 0
    for key in result_room_number:
        result += result_room_number[key]
    return result


def print_each_room_number(last_month_number, current_month_number, result_room_number):
    """
    打印每个房间当月用电度数情况
    :param last_month_number:
    :param current_month_number:
    :param result_room_number:
    :return:
    """
    for key in sorted(current_month_number):
        title = key+'号屋：'
        if cmp(key, '0') == 0:
            title = '公共： '

        print title+str(current_month_number[key]) + ' - ' + str(last_month_number[key]) + ' = ' + str(result_room_number[key])


def print_total_number(result_room_number, result_total_number):
    """
    打印当月使用的电费总度数
    :param result_room_number:
    :param result_total_number:
    :return:
    """
    result = "总度数："
    for key in sorted(result_room_number):
        result += str(result_room_number[key]) + ' '

    # 把空格替换成+，且最后一个不替换
    result = result.replace(' ', ' + ', len(result_room_number)-1)
    result += ' = '
    result += str(result_total_number)

    print result


def print_each_room_fee(room_fee, total_fee, room_number, total_number):
    """
    打印每个房间应缴费情况
    :param room_fee:
    :param total_fee:
    :param room_number:
    :param total_number:
    :return:
    """

    # 房客数量
    num = len(room_fee)

    for key in sorted(room_fee):
        result = key+"号屋："
        result += '( '
        result += str(room_number[key])
        result +=' + '
        result += str(room_number['0'])
        result += ' / '
        result += str(num)
        result += ') / '+str(total_number)+" * "+str(total_fee)+' = '+str(room_fee[key])
        print result


def print_line_seperate_symbol():
    """
    打印行分割符号
    :return:
    """
    print '----------------------------------'


def resove_enter_parameters(parameters):
    """
    解析命令行参数：【脚本名：arg1, arg2, arg3】
    :param parameters:
    :return:
    """

    if len(parameters) != 4 or not isinstance(parameters, list):
        raise Exception("""
        参数不匹配! 
        参数格式：上个月电费度数文件，这个月电费度数文件，这个月电费金额
        例子：bills/2018-01.csv, bills/2018-02.csv, bills/2018-02fee.csv
        """)
    else:
        return parameters[1:]


if __name__ == '__main__':

    try:
        parameters = resove_enter_parameters(argv)
        count_statistics(parameters[0], parameters[1], parameters[2])
        # count_statistics("bills/2018-01.csv", "bills/2018-02.csv", "bills/2018-02fee.csv")
    except Exception, arg:
        print arg
