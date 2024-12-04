import re

file = open('/Users/lkrochma/Git/Github/advent-of-code-repo/resources/04.txt', 'r')
lines = file.read().splitlines()
file.close()


def check(x1, y1, x2, y2, x3, y3, x4, y4):
    if -1 in (x1, y1, x2, y2, x3, y3, x4, y4):
        return False
    try:
        if lines[x1][y1] + lines[x2][y2] in ('MS', 'SM') and lines[x3][y3] + lines[x4][y4] in ('MS', 'SM'):
            return True
        else:
            return False
    except:
        return False

result = 0

for x, line in enumerate(lines):
    for y, char in enumerate(line):
        if char == 'A':
            if check(x-1, y-1, x+1, y+1, x-1, y+1, x+1, y-1):
                result += 1


print(result)