import re

file = open('/Users/lkrochma/Git/Github/advent-of-code-repo/resources/01.txt', 'r')
lines = file.readlines()
file.close()


left = []
right = []

for line in lines:
    l, r = re.findall(r'\d+', line)
    left.append(int(l))
    right.append(int(r))

left.sort()
right.sort()

result = 0

for i in range(len(left)):
    result += abs(left[i] - right[i])

print(result)