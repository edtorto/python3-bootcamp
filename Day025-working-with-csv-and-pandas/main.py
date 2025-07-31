# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

# import csv
#
# with open("weather_data.csv") as csv_file:
#     data = csv.reader(csv_file)
#     temperature = []
#     for row in data:
#         if row[1] != "temp":
#             temperature.append(int(row[1]))
#     print(temperature)

import pandas as pd

data = pd.read_csv("weather_data.csv")
# print(df.head())
# print(df["temp"])

#type check
print(type(data))
print(type(data["temp"]))

#dataframe to dictionary
data_dict = data.to_dict()
print(data_dict)

#series to list
temp_list = data["temp"].to_list()
average_temp = sum(temp_list)/len(temp_list)
print(average_temp)
print(data["temp"].mean())
print(data["temp"].max())

#get data in the column
print(data["condition"])
print(data.condition)

#get data in rows
print(data[data.day == "Monday"])
print(data[data.temp == data.temp.max()])

#get a particular value of a selected column
monday = data[data.day == "Monday"]
print(monday.condition)

# convert from C to F
mon_temp = int(monday.temp)
mon_temp_F = mon_temp * 9/5 + 32
print(mon_temp_F)

#create a dataframe from scratch
data_dict = {
    "student": ["Tom", "Jerry","John"],
    "score": [52, 43, 90],
}
student_df = pd.DataFrame(data_dict)
print(student_df)

#save to a csv file
student_df.to_csv("student_data.csv")