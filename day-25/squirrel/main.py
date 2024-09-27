# import csv

# with open("weather_data.csv") as weather_data_file:
#     data = csv.reader(weather_data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

# import pandas
# data = pandas.read_csv("weather_data.csv")
# <class 'pandas.core.frame.DataFrame'>
# print(type(data))
# <class 'pandas.core.series.Series'>
# print(type(data["temp"]))

# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data["temp"].to_list()

# mean = sum(temp_list) / len(temp_list)
# print(mean)

# print(data["temp"].mean())
# print(data["temp"].max())

# Get data in column 
# print(data["condition"])
# print(data.condition)

# Get data in row
# print(data[data.day == "Monday"])
# print(data[data.temp == data["temp"].max()])
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# print(monday.condition)

# monday_temp_farenheit = monday.temp[0] * 9/5 + 32
# print(monday_temp_farenheit)


# Create a dataframe from scratch
# data_dict = {
#     "student": ["Amy", "James","Angela"],
#     "scores": [76, 56, 65]
# }

# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")

import pandas

data = pandas.read_csv("squirrel_count.csv")
# print(data["Primary Fur Color"].value_counts())

#same effect manually

# print((data["Primary Fur Color"] == "Gray").sum())
gray_squirrel_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrel_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrel_count = len(data[data["Primary Fur Color"] == "Black"])

print(gray_squirrel_count)
print(red_squirrel_count)
print(black_squirrel_count)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrel_count, red_squirrel_count, black_squirrel_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count_per_color.csv")