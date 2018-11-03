# -*- coding: UTF-8 -*-

import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime as dt


def plot_date_fee():
    """
    绘制日期和电费之间的关系曲线
    :return:
    """
    fee_list = [19.98, 17.24, 26.46, 66.73, 78.38, 30.56, 40.51, 33.53, 26.87, 35.42, 39.18, 50.82, 33.98, 25.16]
    date_list = ["2017-09", "2017-10", "2017-11", "2017-12", "2018-01", "2018-02", "2018-03", "2018-04", "2018-05", "2018-06", "2018-07", "2018-08", "2018-09", "2018-10"]

    xdate_list = [dt.datetime.strptime(d, '%Y-%m').date() for d in date_list]

    fig, ax = plt.subplots()
    ax.plot(xdate_list, fee_list, 'b^--')

    # 设置主刻度标签的文本已经位置
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))
    ax.xaxis.set_major_locator(mdates.MonthLocator())

    ax.format_xdate = mdates.DateFormatter('%Y-%m')
    ax.grid(True)

    fig.autofmt_xdate()
    plt.show()


def plot_degree_fee():
    """
    绘制度数与电费之间的关系
    :return:
    """

    degree_list = [36, 32, 63, 158, 186, 52, 73, 43, 52, 72, 69, 106, 58, 38]
    fee_list = [19.98, 17.24, 26.46, 66.73, 78.38, 30.56, 40.51, 33.53, 26.87, 35.42, 39.18, 50.82, 33.98, 25.16]

    plt.plot(degree_list, fee_list, 'ro')

    plt.grid(True)

    plt.xlabel("degree")
    plt.ylabel("fee")
    plt.show()


if __name__ == '__main__':
    # 绘制日期和电费之间的关系曲线
    plot_date_fee()

    # 绘制度数与电费之间的关系
    plot_degree_fee()
