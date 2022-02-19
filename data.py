
import csv
import math


with open('data.csv',newline='') as f:
    reader = csv.reader(f)
    file_data = list(reader)
data = file_data[0]

n = len(data)

def mean(data):
    total = 0
    for i in data:
        total+=int(i)
    mean = total/n
    return mean

sq_list = []
for x in data:
    a = int(x)-mean(data)
    b = a**2
    sq_list.append(b)
sum = 0
for y in sq_list:
    sum+=y

divided = sum/(n-1)
std_deviation = math.sqrt(divided)

print(std_deviation)