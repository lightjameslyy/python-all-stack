hello_str = "hello world"

print(hello_str.startswith("Hello"))
print(hello_str.endswith("d"))

print(hello_str.find("llo"))  # same as index
print(hello_str.find("abc"))  # diff from index

print(hello_str.replace("world", "python"))  # replace 是值传递
print(hello_str)
