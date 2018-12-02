"""
Isaac Sutor
AdventofCode.com Day 1 Part 1
12/1/2018
"""

filename = "dayone"
file = open(filename)
freq = 0
for line in file:
    freq += int(line)

print(freq)
file.close()
