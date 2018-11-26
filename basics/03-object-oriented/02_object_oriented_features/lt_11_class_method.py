class Tool(object):
    # 类属性
    count = 0

    @classmethod
    def show_tool_count(cls):
        print("Tool的对象的数量：%d" % cls.count)

    def __init__(self, name):
        self.name = name

        Tool.count += 1


tool1 = Tool("斧头")

Tool.show_tool_count()

tool2 = Tool("榔头")

Tool.show_tool_count()
