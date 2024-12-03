import re

file = open('/Users/lkrochma/Git/Github/advent-of-code-repo/resources/02.txt', 'r')
lines = file.read().splitlines()
file.close()

        
result = 0

for line in lines:
    values = [int(x) for x in re.findall(r'\d+', line) ]
    safe = True
    previous_value = None
    ascending = None
    for value in values:
        if previous_value != None:
            if abs(previous_value - value) < 1 or abs(previous_value - value) > 3:
                safe = False
                break
            if ascending == None:
                ascending = previous_value < value
            elif ascending:
                safe = previous_value < value
            else:
                safe = previous_value > value
        previous_value = value
        if not safe:
            break
    if safe:
        result += 1

print(result)