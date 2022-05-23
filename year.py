import csv
import matplotlib.pylab as plt
data = []
with open("Maharashtra.csv", 'r', encoding="unicode_escape") as csvfile:
    reader_variable = csv.reader(csvfile)
    for row in reader_variable:
        data.append(row)
n = len(data)
Dict = {}
a = 0
for i in range(1, n):
    b = (data[i][6]).strip()
    if len(b) > 4:
        c, d, e = b.split('-')
        year = ""
        if(len(b) == 8):
            x = int(e)
            if(x >= 0 and x <= 20):
                year = "20" + e
            else:
                year = "19" + e
        if(len(b) == 10):
            year = c

        if year in Dict.keys():
            Dict[year] += 1
        else:
            Dict[year] = 1
year = []
car = []
for i in sorted(Dict.keys()):
    if(Dict[i] > 500):
        year.append(i)
        car.append(Dict[i])
plt.barh(year, car)
plt.xlabel("population of saarc countries")
plt.ylabel("year")
plt.show()
# completed
