import csv
import matplotlib.pylab as plt
data = []
with open("Maharashtra.csv", 'r', encoding="unicode_escape") as csvfile:
    reader_variable = csv.reader(csvfile)
    for row in reader_variable:
        data.append(row)
n = len(data)
m = len(data[0])
lessThanOneLack = 0
lessThanTenLacks = 0
lessThenOneCr = 0
lessThanTenCr = 0
greaterThanTenCr = 0
for i in range(1, n):
    a = float(data[i][8])
    if(a <= 100000):
        lessThanOneLack += 1
    elif a <= 1000000:
        lessThanTenLacks += 1
    elif a <= 10000000:
        lessThenOneCr += 1
    elif a <= 100000000:
        lessThanTenCr += 1
    else:
        greaterThanTenCr += 1
x = ["<=1L", "<=10L", "<=1Cr", "<=10Cr", ">10Cr"]
y = [lessThanOneLack, lessThanTenLacks, lessThenOneCr,
                    lessThanTenCr, greaterThanTenCr]
plt.bar(x, y)
plt.show()
# This is completed
