# open
file_read = open("README")
file_write = open("README_cpy", "w")

# read and write
text = file_read.read()
file_write.write(text)

# close
file_read.close()
file_write.close()
