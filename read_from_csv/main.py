# with open("./read_from_csv/weather_data.csv") as weather_data_csv:
#    data = weather_data_csv.readlines()
#    print(data)
#

# import csv
#
# with open("./read_from_csv/weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#
#     print(temperatures)

import pandas

# data = pandas.read_csv("./read_from_csv/weather_data.csv")
# print(type(data))
# print(type(data["temp"]))
# print(data["temp"])
#
# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data["temp"].tolist()
# print(temp_list)
#
# avg_temp = sum(temp_list) / len(temp_list)
# print(avg_temp)
#
# average_temp = data["temp"].mean()
# print(average_temp)
#
# max_temp = data["temp"].max()
# print(max_temp)
#
# print(data.condition)
#
# Get data in a row
# print(data[data["day"] == "Monday"])

# Get a row with highest temperatue
# print(data[data.temp == data.temp.max()])


# monday = data[data.day == "Monday"]
# monday_temp = monday.temp[0]
#
# monday_temp_in_farenheit = monday_temp * 9 / 5 + 32
# print(monday_temp_in_farenheit)
#
# Create dataframe  from scratch
data_dict = {"students": ["Amy", "James", "Angela"], "scores": [76, 56, 65]}

new_data = pandas.DataFrame(data_dict)
print(new_data)
new_data.to_csv("./read_from_csv/students.csv")
