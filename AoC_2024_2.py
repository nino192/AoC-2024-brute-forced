#!/usr/bin/python3

# 318!

f = open("AoC_2024_2.txt","r")
lists = f.readlines()
count = 0

def problem_dampener(x, count):
    for i in range(len(x)):
        povecalo = False
        smanjilo = False
        x_copy = x.copy()
        x_copy.pop(i)
        prev = x_copy[0]
        for i in range(1, len(x_copy)):
            tren = x_copy[i]
            razlika = prev - tren
            razlika_abs = abs(prev - tren)
            prev = tren
            if (razlika_abs == 0) or (razlika_abs > 3):
                break
            if razlika < 0:
                povecalo = True
            if razlika > 0:
                smanjilo = True
            if (smanjilo == True) and (povecalo == True):
                break
            if i == (len(x_copy) - 1):
                count = count + 1
                return count
    return count



for x in lists:
    x = x.split(' ')
    x = [int(item) for item in x]
    prev = x[0]
    povecalo = False
    smanjilo = False
    for i in range(1, len(x)):
        tren = x[i]
        razlika = prev - tren
        razlika_abs = abs(prev - tren)
        if razlika_abs == 0 or razlika_abs > 3:
            count = problem_dampener(x, count)
            break
        if razlika < 0:
            povecalo = True
        if razlika > 0:
            smanjilo = True
        if (smanjilo == True) and (povecalo == True):
            count = problem_dampener(x, count)
            break
        prev = tren
        if i == (len(x)-1):
            count = count + 1
            break

print(count)

            