name_list = ["zhangsan", "lisi", "wangwu"]
print(name_list)

# 1. 取值和取索引
print(name_list[2])
print(name_list.index("zhangsan"))

# 2. 修改
name_list[1] = "李四"
print(name_list)

# 3. 增加
name_list.append("王小二")
print(name_list)

name_list.insert(1, "小明")
print(name_list)

tmp_list = ["孙悟空","猪八戒","沙和尚"]
name_list.extend(tmp_list)
print(name_list)

# 4. 删除
name_list.remove("wangwu")
print(name_list)

name_list.pop()
print(name_list)

name_list.pop(3)
print(name_list)

del name_list[2]

name_list.clear()
print(name_list)

