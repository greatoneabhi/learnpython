numbers = [1, 2, 3]
# new_list = []
# for n in numbers:
#     add_1 = n + 1
#     new_list.append(add_1)
#
# print(new_list)
#
# new_list = [new_item for item in list]
new_list = [n + 1 for n in numbers]
print(new_list)

name = "Angela"
letters_list = [letter for letter in name]
print(letters_list)

range_list = [n * 2 for n in range(1, 5)]
print(range_list)

# new_list = [new_item for item in list if test]
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
short_names = [name for name in names if len(name) < 5]
print(short_names)

uppercase_long_names = [name.upper() for name in names if len(name) > 5]
print(uppercase_long_names)
