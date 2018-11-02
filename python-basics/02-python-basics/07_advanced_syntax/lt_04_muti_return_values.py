def measure():
    """
    测量温度和湿度
    :return:
    """

    temp = 39
    wetness = 50

    # return (temp, wetness)  # 返回元组，括号可以省略
    return temp, wetness


result = measure()
print(result)

gl_temp, gl_wetness = measure()
print(gl_temp, gl_wetness)
