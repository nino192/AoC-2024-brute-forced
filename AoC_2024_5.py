instructions = []
updates_l = []
with open('AoC_2024_5.txt', 'r') as file:
    data = file.read().splitlines()
    updates_str = data[1177:1373]
    for element in updates_str:
        element = element.split(',')
        updates_l.append(element)
    for line in data:
        if line:
            instructions.append(line.split("|"))
        else:
            break

def check_function(instructions, element, current, slice, length, total, i):
    bad = False
    for instance in instructions:
        if (instance[1] in slice) and instance[0] == current:
            bad = True
            return total, bad

        else:
            if i == (length-1) and instance == instructions[-1]:
                total = total + int(element[(length-1)//2])
                return total, bad
    return total, bad

total = 0

for element in updates_l:
    length = len(element)
    for i in range(length):
        current = element[i]
        slice = element[:i]
        total, bad = check_function(instructions, element, current, slice, length, total, i)
        if bad:
            break

print(total)