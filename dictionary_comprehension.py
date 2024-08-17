# new_dict = {new_key:new_value for item in list if test}
# new_dict = {new_key:new_value for (key, value) in dict.items() if test}

import random

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
students_scores = {student: random.randint(1, 100) for student in names}
print(students_scores)

passed_students = {
    key: value for (key, value) in students_scores.items() if value >= 40
}
print(passed_students)
