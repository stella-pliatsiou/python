import re

#Extracting Digits and Summing them
hand = open("regex_sum_1091501.txt")
numlist = []

for line in hand:
    line = line.rstrip()
    extract = re.findall("([0-9]+)", line)

    if len(extract) < 1 : continue

    for i in range(len(extract)):
        num = float(extract[i])
        numlist.append(num)

print(sum(numlist))
