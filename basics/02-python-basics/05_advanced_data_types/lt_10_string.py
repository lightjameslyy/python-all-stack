str1 = "hello python"
str2 = 'hello "python"'

print(str2)
print(str1[6])

# 遍历
for ch in str1:
    print(ch, end="-")
print("")

# len
print(len(str1))

# count
print(str1.count("llo"))
print(str1.count("lloo"))

# index
print(str1.index("llo"))
print(str1.index("lloo"))
