input_str = input("请输入算术题：")

print(eval(input_str))

# 如果输入的是系统命令，会很危险！
# e.g.: input_str = "__import__('os').system('危险的终端命令')"