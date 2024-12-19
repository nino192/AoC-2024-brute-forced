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

def sort_function(element, instructions):
    bad = True
    c = 0
    while bad or c < (len(element)-1):
        current = element[c]
        slice = element[:c]
        for instance in instructions:
            if (instance[1] in slice) and instance[0] == current:
                element[len(slice)], element[len(slice)-1] = element[len(slice)-1], element[len(slice)]
                c = 0
                break
            elif c == (len(element)-1) and instance == instructions[-1]:
                bad = False
                break
        c = c + 1
    element_sorted = element
    return element_sorted

total = 0
total_2 = 0

for element in updates_l:
    length = len(element)
    for i in range(length):
        current = element[i]
        slice = element[:i]
        total, bad = check_function(instructions, element, current, slice, length, total, i)
        if bad:
            element_sorted = sort_function(element, instructions)
            total_2 = total_2 + int(element_sorted[(length-1)//2])
            break

print(total, total_2)