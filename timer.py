import datetime as dt
import pandas
from pandas import DataFrame as df
import matplotlib.pyplot as plt

try:
    data_file = pandas.read_csv("data.csv", header=0)
except:
    data_file = df

# results = {
#     "date": [],
#     "type_of_work": [],
#     "time": []
# }

# while(True):
#     type_of_work = input(
#     """what do you work on?
#     [1] Solve puzzles & watch video
#     [2] Work on Python course
#     """)

#     try:
#         type_of_work = int(type_of_work)
#     except ValueError:
#         type_of_work = 0

#     if type_of_work in range (1, 5):
#         type_of_work = type_of_work
#         break
#     else:
#         print("You have to choose number between 1 - 4 (both included)")

# print(f"You have choosen {type_of_work}. Now let's start!")

# start = dt.datetime.now()
# user_choice = input("Press x when you'll finish: ")
# stop = dt.datetime.now()


# results["date"].append(dt.date.today().isoformat())
# results["type_of_work"].append(type_of_work)
# results["time"].append((stop - start).seconds)


# results_df = df.from_dict(results)
# data_file = data_file.append(results_df, ignore_index=True)
# print(results_df)
# data_file.to_csv("data.csv", index=False)



print(data_file)
# plot = data_file.type_of_work.value_counts().plot(kind="pie")
# plot = data_file.plot(x='type_of_wok', y='time', figsize=(5, 5), kind='pie')

labels = data_file["type_of_work"].tolist()
times = data_file["time"].tolist()
colors = ["gold", "yellow", "green"]

plt.pie(times, labels=labels, colors=colors, autopct="%1.1f%%")
plt.show()

# # Data to plot
# labels = 'Python', 'C++', 'Ruby', 'Java'
# sizes = [215, 130, 245, 210]
# colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']
# explode = (0.1, 0, 0, 0)  # explode 1st slice

# # Plot
# plt.pie(sizes, explode=explode, labels=labels, colors=colors,
# autopct='%1.1f%%', shadow=True, startangle=140)

# plt.axis('equal')
# # plt.show()




