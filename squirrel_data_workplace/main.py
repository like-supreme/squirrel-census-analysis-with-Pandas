"""https://data.cityofnewyork.us/Environment/2018-Central-Park-Squirrel-Census-Squirrel-Data/vfnx-vebw/about_data
central park squirrel data"""
# koskoca verisetinden Primary Fur Color alacağız sayısını sayıp tabloya ekleyeceğiz

import pandas as pd

data = pd.read_csv("day25/end/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
fur_color = data["Primary Fur Color"]

black_squirrels = 0
gray_squirrels = 0
cinnamon_squirrels = 0



for i in fur_color:
    if i == "Black":
        black_squirrels += 1
    
    elif i == "Gray":
        gray_squirrels += 1

    elif i == "Cinnamon":
        cinnamon_squirrels += 1
    
    else: 
        continue

print(f" Black : {black_squirrels}")
print(f" Gray : {gray_squirrels}")
print(f" Cinnamon : {cinnamon_squirrels}")

data_dict = {
    "Fur Color" : ["Gray" , "Black" , "Cinnamon"] , 
    "Count" : [gray_squirrels , black_squirrels , cinnamon_squirrels]
}
new_data = pd.DataFrame(data_dict)
new_data.to_csv("fur_color_and_count.csv")

