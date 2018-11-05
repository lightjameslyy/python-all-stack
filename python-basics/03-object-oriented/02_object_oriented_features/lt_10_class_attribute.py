class Tool(object):
    # 类属性
    count = 0

    def __init__(self, name):
        self.name = name

        Tool.count += 1


tool1 = Tool("斧头")

print(Tool.count)

tool2 = Tool("榔头")
tool3 = Tool("水桶")

print(Tool.count)

# 通过实例对象也可以获取类属性，但是不推荐
print(tool1.count)
print(tool2.count)
print(tool3.count)

# 陷阱！！！不能用实例对象改变类属性。结果是实例对象创建同名的属性，不会改变类的属性！
tool3.count = 99
print("count in tool3: %d" % tool3.count)
print("count in Tool: %d" % Tool.count)
