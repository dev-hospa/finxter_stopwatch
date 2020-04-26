import datetime as dt
import pandas
from pandas import DataFrame as df
import matplotlib.pyplot as plt


# Check if data.csv exists
try:
    data_file = pandas.read_csv("data.csv", header=0)
except:
    data_file = df

results = {
    "date": [],
    "type_of_work": [],
    "time": []
}

while(True):
    type_of_work = input(
    """what do you work on?
    [1] Solve puzzles & watch video
    [2] Work on Python course
    [3] Read Relevant Docs & Libraries
    [4] Work on Practical Python Projects
    """)

    try:
        type_of_work = int(type_of_work)
    except ValueError:
        type_of_work = 0

    if type_of_work in range (1, 5):
        type_of_work = type_of_work
        break
    else:
        print("You have to choose number between 1 - 4 (both included)")

print(f"You have choosen {type_of_work}. Now let's start!")

# 
start = dt.datetime.now()
user_choice = input("Press x when you'll finish: ")
stop = dt.datetime.now()

# save the time
results["date"].append(dt.date.today().isoformat())
results["type_of_work"].append(type_of_work)
results["time"].append((stop - start).seconds)

# create dataframe from results
results_df = df.from_dict(results)
data_file = data_file.append(results_df, ignore_index=True)
pivot = data_file.groupby(["type_of_work"]).sum()
data_file.to_csv("data.csv", index=False)

# Create pie chart
labels = ["[1] Solve Puzzles & Watch Video", "[2] Work on Python Course", "[3] Read Relevant Docs & Libraries", "[4] Work on Practical Python Projects"]    
times = pivot["time"].tolist()
colors = ["lightblue", "violet", "gold", "green"]

plt.pie(times, labels=labels, colors=colors, autopct="%1.1f%%")
plt.savefig("chart.png")
plt.show()
