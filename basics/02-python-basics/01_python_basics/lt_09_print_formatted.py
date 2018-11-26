# var name, print "my name is <name>"
name = "terry leo"
print("my name is %s" % name)

# student_no, at most 6 digits preceded with 0s
student_no = 1
print("my student No is %06d" % student_no)

# buy apples
price = 8.5
weight = 7.5
money = price * weight
print("苹果单价：%.2f 元/斤，买了 %.2f 斤，需支付 %.2f 元" % (price, weight, money))

# scale
scale = 0.25
print("数据比例是 %.2f%%" % (scale * 100))
