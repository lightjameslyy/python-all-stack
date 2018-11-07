# 1. open
file = open("README")

# 2. read
text = file.read()
print(text)
print(len(text))

print("-" * 50)

# file pointer at end of file
text = file.read()
print(text)
print(len(text))

# 3. close
file.close()
