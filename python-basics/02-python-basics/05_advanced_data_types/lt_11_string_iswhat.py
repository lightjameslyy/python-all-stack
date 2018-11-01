# isspace
space_str = "   \t \n \r"
print(space_str.isspace())

# isnum isdigit isdecimal
# num_str = "1.7"
# num_str = "⑴"  # unicode string
# num_str = "\u00b2"
num_str = "百"

print(num_str)
print(num_str.isdecimal())
print(num_str.isdigit())
print(num_str.isnumeric())
