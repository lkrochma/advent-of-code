import re

file = open('/Users/lkrochma/Git/Github/advent-of-code-repo/resources/04.txt', 'r')
lines = file.read().splitlines()
file.close()


def check(x1, y1, x2, y2, x3, y3):
    if -1 in (x1, y1, x2, y2, x3, y3):
        return False
    try:
        if lines[x1][y1] == 'M' and lines[x2][y2] == 'A' and lines[x3][y3] == 'S':
            return True
        else:
            return False
    except:
        return False

def searchForResults(x, y):
    hits = 0
    # horizontal 1
    if check(x, y+1, x, y+2, x, y+3):
        hits +=1
    # horizontal 2
    if check(x, y-1, x, y-2, x, y-3):
        hits += 1
    # vertical 1
    if check(x+1, y, x+2, y, x+3, y):
        hits += 1
    # vertical 2
    if check(x-1, y, x-2, y, x-3, y):
        hits += 1
    # diagonal 1
    if check(x+1, y+1, x+2, y+2, x+3, y+3):
        hits += 1
    # diagonal 2
    if check(x+1, y-1, x+2, y-2, x+3, y-3):
        hits += 1
    # diagonal 3
    if check(x-1, y-1, x-2, y-2, x-3, y-3):
        hits += 1
    # diagonal 4
    if check(x-1, y+1, x-2, y+2, x-3, y+3):
        hits += 1
    return hits

result = 0

for x, line in enumerate(lines):
    for y, char in enumerate(line):
        if char == 'X':
            result += searchForResults(x, y)


print(result)