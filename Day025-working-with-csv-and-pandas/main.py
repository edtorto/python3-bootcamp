#using readlines() method on csv
with open("weather_data.csv") as data_file:
    w_data = data_file.readlines()
    print(w_data)

#using csv library
import csv
with open("weather_data.csv") as csv_file:
    csv_data = csv.reader(csv_file)
    temperature = []
    for row in csv_data:
        if row[1] != "temp":
            temperature.append(int(row[1]))
    print(temperature)

#using pandas library
import pandas as pd
data = pd.read_csv("weather_data.csv")
print(data.head())
print(data["temp"])

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

#create a csv file from another csv file
#read data
squirrel_data = pd.read_csv("2018_Squirrel_Data.csv")

#count number of different fur colors
gray_color_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Gray"])
cinnamon_color_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Cinnamon"])
black_color_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Black"])

#create the dictionary
color_dic = {
    "color": ["Gray", "Cinnamon", "Black"],
    "count": [gray_color_count, cinnamon_color_count, black_color_count]
}

# convert to dictionary to dataframe
df = pd.DataFrame(color_dic)

#save dataframe to csv file
df.to_csv("squirrel_color_count.csv")