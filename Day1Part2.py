"""
Isaac Sutor
AdventofCode.com Day 1 Part 2
12/1/2018
"""

filename = "dayone"
file = open(filename)
arrvals = []

for line in file:
    arrvals.append(int(line))
file.close()

# switched to set because list takes too long to search
def search_set(li):
    seen = set()
    s = 0
    while True:
        for i in li:
            if s in seen:
                return s
            seen.add(s)
            s += i


print(search_set(arrvals))

