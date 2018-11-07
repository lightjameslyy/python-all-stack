# open
file_read = open("README")
file_write = open("README_cpy", "w")

# read and write
while True:
    text = file_read.readline()

    if not text:
        break

    file_write.write(text)

# close
file_read.close()
file_write.close()
