import re

file = open('/Users/lkrochma/Git/Github/advent-of-code-repo/resources/02.txt', 'r')
lines = file.read().splitlines()
file.close()

        
result = 0
unsafe = []

def checkSafe(values):
    safe = True
    previous_value = None
    ascending = None
    for value in values:
        if previous_value != None:
            if abs(previous_value - value) < 1 or abs(previous_value - value) > 3:
                return False
            if ascending == None:
                ascending = previous_value < value
            elif ascending:
                safe = previous_value < value
            else:
                safe = previous_value > value
        previous_value = value
        if not safe:
            break
    return safe
    

for line in lines:
    values = [int(x) for x in re.findall(r'\d+', line) ]
    isSafe = checkSafe(values)
    if isSafe:
        result += 1
    else:
        unsafe.append(values)
    
for report in unsafe:
    for i, level in enumerate(report):
        new_report = list(report)
        new_report.pop(i)
        isSafe = checkSafe(new_report)
        if isSafe:
            result += 1
            break

print(result)