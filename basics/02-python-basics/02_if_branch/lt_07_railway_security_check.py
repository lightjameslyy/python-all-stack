# 是否有票
has_ticket = True

# 刀的长度，厘米
knife_length = 30

if has_ticket:
    print("有车票，开始安检...")
    if knife_length <= 20:
        print("安检通过，请上车")
    else:
        print("您携带的刀太长，有%d厘米长，不允许上车！" % knife_length)
else:
    print("大哥，请先买票")

