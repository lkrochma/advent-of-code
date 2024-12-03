import re

file = open('/Users/lkrochma/Git/Github/advent-of-code-repo/resources/03.txt', 'r')
file_content = file.read()
file.close()


result = 0
operations = []
operations.extend(re.findall(r'mul\(\d+\,\d+\)', file_content))

for operation in operations:
    l,r = [int(x) for x in re.findall(r'\d+', operation)]
    result += l * r


print(result)