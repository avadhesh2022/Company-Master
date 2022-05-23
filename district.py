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
# first colomn does not contain zipcode
for i in range(n):
    x = (data[i][6]).strip()
    if len(x) == 8:
        a, b, c = x.split('-')
        if(c == "15"):
            y = data[i][12].split()
            zip = y[-1]
            if(zip.isdigit()):
                if zip in Dict.keys():
                    Dict[zip] += 1
                else:
                    Dict[zip] = 1
print(len(Dict))
district = []
car = []
for i in sorted(Dict.keys()):
    if(Dict[i] > 100):
        district.append(i)
        car.append(Dict[i])

plt.barh(district, car)
plt.xlabel("Number of cars")
plt.ylabel("zip code of top district")
plt.show()
# completed
