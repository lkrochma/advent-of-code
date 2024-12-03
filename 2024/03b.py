import re

file = open('/Users/lkrochma/Git/Github/advent-of-code-repo/resources/03.txt', 'r')
file_content = file.read()
file.close()


result = 0
operations = re.findall(r'(mul\(\d+\,\d+\)|do\(\)|don\'t\(\))', file_content)


eval = True
for operation in operations:
    if operation == 'do()':
        eval = True
    elif operation == 'don\'t()':
        eval = False
    elif eval:
        l,r = [int(x) for x in re.findall(r'\d+', operation)]
        result += l * r


print(result)