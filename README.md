# squirrel-census-analysis-with-Pandas
Analyze squirrel fur color distribution in Central Park using a real NYC dataset with Python and pandas. Data visualization-ready output CSV included.

# 🐿️ Central Park Squirrel Fur Color Census

This mini project analyzes the fur color distribution of squirrels in Central Park using real data from the [2018 Central Park Squirrel Census](https://data.cityofnewyork.us/Environment/2018-Central-Park-Squirrel-Census-Squirrel-Data/vfnx-vebw). The goal is to count how many squirrels have Gray, Black, or Cinnamon fur and export the results into a new CSV file.

## 📂 Dataset

The dataset contains thousands of rows and dozens of features collected during a census of squirrels in NYC's Central Park. Each row represents an individual squirrel sighting, with information such as fur color, age, activity, location, and more. 


- Source: NYC Open Data
- File: `2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv`
- If you want to learn more about the experiment. "https://data.cityofnewyork.us/Environment/2018-Central-Park-Squirrel-Census-Squirrel-Data/vfnx-vebw/about_data"

## 🧠 What This Project Does

- Uses **pandas** to read and process the dataset.
- Iterates through the `"Primary Fur Color"` column.
- Counts the number of squirrels by each fur color:
  - Gray
  - Black
  - Cinnamon
- Outputs the result as a new CSV file: `fur_color_and_count.csv`

## 📊 Output Example

| Fur Color | Count |
|-----------|-------|
| Gray      | 2473  |
| Black     | 103   |
| Cinnamon  | 392   |

*(Note: actual counts may vary based on dataset version)*

## 📁 File Structure

├── 2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv
├── main.py
├── fur_color_and_count.csv
## 🚀 How to Run

1. Clone the repo
2. Install requirements (just `pandas`) in terminal just write pip install pandas
3. Run:
 
python main.py
You will get a new CSV file containing the squirrel color distribution.

🤔 Why This Matters
This project is a great beginner-friendly exercise for working with real-world data using Python. It teaches:

CSV file operations

Looping through DataFrames

Basic data aggregation

Creating DataFrame , creating a csv file and Exporting data
