xiaoming = {
    "name": "小明",
    "age": 18,
    "gender": True,
    "height": 1.75,
    "weight": 75.5,
}

print(xiaoming)

# 1. 取值
print(xiaoming["name"])

# 2. 增加/修改
xiaoming["age"] = 25
print(xiaoming)

xiaoming["hobby"] = "basketball"
print(xiaoming)

# 3. 删除
xiaoming.pop("hobby")
print(xiaoming)

# 4. len
print(len(xiaoming))

# 5. 合并字典
tmp_dict = {"height": 1.80}
xiaoming.update(tmp_dict)
print(xiaoming)

# 6. clear
# xiaoming.clear()
# print(xiaoming)

# 7. 遍历
for k in xiaoming:
    print(k, "-", xiaoming[k])
