import pandas

student_dict = {"student": ["Angela", "James", "Lily"], "score": [56, 76, 98]}

# looping through dictionaries
# for key, value in student_dict.items():
#     print(f"key: {key}, value: {value}")


student_data_frame = pandas.DataFrame(student_dict)

# loop through data ftame
# for key, value in student_data_frame.items():
#     print(value)
#
for index, row in student_data_frame.iterrows():
    print(f"{row.student} {row.score}")
