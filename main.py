from io import StringIO
import csv

def task(csvString):
    f = StringIO(csvString)
    reader = csv.reader(f, delimiter=',')
    input = []
    for i in reader:
        input.append(i)
    r = []
    r1 = []
    r2 = []
    r3 = []
    r4 = []
    r5 = []
    for i in input:
        if i[0] not in r1:
            r1.append(i[0])
    for i in input:
        if i[1] not in r2:
            r2.append(i[1])
    for i in input:
        for j in input:
            if i[0] not in r3 and j[0] == i[1]:
                r3.append(i[0])
    for i in input:
        for j in input:
            if i[1] not in r4 and j[1] == i[0]:
                r4.append(i[1])
    for i in input:
        for j in input:
            if i[1] not in r5 and j[0] == j[0] and j != i:
                r5.append(i[1])
    r.append(r1)
    r.append(r2)
    r.append(r3)
    r.append(r4)
    r.append(r5)
    return r

with open('data.csv') as file:
    csvString = file.read()
    result = task(csvString)
    print(result)
