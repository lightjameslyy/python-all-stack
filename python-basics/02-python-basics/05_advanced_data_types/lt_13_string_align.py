poem = [
    "\t\n登鹳雀楼",
    "王之涣",
    "白日依山尽\t\n",
    "黄河入海流",
    "欲穷千里目",
    "更上一层楼"
]

for str in poem:
    # print("|%s|" % str.center(10, "　"))
    # print("|%s|" % str.ljust(10, "　"))
    print("|%s|" % str.strip().rjust(10, "　"))
