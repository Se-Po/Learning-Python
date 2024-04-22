first_name = "sebastian"
last_name = " popa"
print(f"Hello {first_name.title()}, would you like to learn some Python today?")

full_name = f"{first_name.title()} {last_name.title().lstrip()}"
print(full_name)

print("My name in UPPER case is", full_name.upper())
print("My name in lower case is", full_name.lower())
print("My name in Title case is", full_name.title())

# 2-5
message = "\tAlbert Einstein once said, \n'A person who never made a mistake never tried anything new'"
print(message)

# 2-8
filename = "new_text.txt"
shortname = filename.removesuffix(".txt")
print(shortname)
