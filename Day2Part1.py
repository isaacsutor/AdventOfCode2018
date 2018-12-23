"""
Isaac Sutor
AdventofCode.com Day 2 Part 1
12/4/2018
"""

filename = "daytwotest"
file = open(filename)
arrvals = []

for line in file:
    arrvals.append(line)
file.close()

dictionary = {
    'a': 0
}

for item in arrvals:
    for letter in item:
        # if contains
        if letter in dictionary:
            print("add letter")
            dictionary[letter] += 1
        # if not contains letter
        else:
            dictionary[letter] = 1
            print("new letter")

del dictionary['\n']
print(dictionary)

dict2 = {
    "twos":  0,
    "threes": 0,
    "fours": 0,
    "fives": 0,
    "sixes": 0
}
for i in dictionary:
    if dictionary[i] == 2:
        dict2["twos"] += 1
        print("added two")
    elif dictionary[i] == 3:
        dict2["threes"] += 1
        print("added three")
    elif dictionary[i] == 4:
        dict2["fours"] += 1
        print("added four")
    elif dictionary[i] == 5:
        dict2["fives"] += 1
        print("added five")
    elif dictionary[i] == 6:
        dict2["sixes"] += 1
        print("added six")

print(dict2)
checksum = 1
for i in dict2:
    if dict2[i] > 0:
        # print(dict2[i])
        checksum *= dict2[i]

print(checksum)
