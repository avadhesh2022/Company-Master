import csv
import matplotlib.pylab as plt
import numpy as np
data = []
with open("Maharashtra.csv", 'r', encoding="unicode_escape") as csvfile:
    reader_variable = csv.reader(csvfile)
    for row in reader_variable:
        data.append(row)
n = len(data)
year = {}
activity = {}
for i in range(1, n):
    b = (data[i][6]).strip()
    if len(b) == 8:
        y = ""
        c, d, e = b.split('-')
        y = "19" + e
        if y in year.keys():
            year[y] += 1
        else:
            year[y] = 1
        if y in activity.keys():
            activity[y] += 1
        else:
            activity[y] = 1
list_year = []
list_activity = []
for i in sorted(year.keys()):
    list_year.append(year[i])
for i in sorted(activity.keys()):
    list_activity.append(activity[i])
x = np.arange(100)
width = 0.2
plt.bar(x-0.1, list_year, width, color='red')
plt.bar(x+0.1, list_activity, width, color='blue')
plt.legend(['registration per year', 'principal business activity'])
plt.xlabel("year from 1900 to 1999")
plt.ylabel("count of principal activity")
plt.show()
