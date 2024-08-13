import pandas

squirrel_data = pandas.read_csv(
    "./squirrel_census/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv"
)

gray_squirrel_data = squirrel_data[squirrel_data["Primary Fur Color"] == "Gray"]
gray_squirrel_count = len(gray_squirrel_data)

black_squirrel_data = squirrel_data[squirrel_data["Primary Fur Color"] == "Black"]
black_squirrel_count = len(black_squirrel_data)

red_squirrel_data = squirrel_data[squirrel_data["Primary Fur Color"] == "Cinnamon"]
red_squirrel_count = len(red_squirrel_data)

# squirrel_count_dict = [
#     {"Fur color": "grey", "count": gray_squirrel_count},
#     {"Fur color": "red", "count": red_squirrel_count},
#     {"Fur color": "black", "count": black_squirrel_count},
# ]

squirrel_count_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrel_count, red_squirrel_count, black_squirrel_count],
}

pandas.DataFrame(squirrel_count_dict).to_csv("./squirrel_census/squirrel_count.csv")
