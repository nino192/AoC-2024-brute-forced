#!/usr/bin/python3
import re

matches = []
def repl(m):                       
    matches.append(m.group())       
    return "{}\n".format(m.group())

with open('AoC_2024_3.txt', 'r') as file:
    data = file.read().replace('\n', '')

mnozi = True
res = 0
exp = r"mul\([0-9]+,[0-9]+\)"
enable = r"do\(\)"
disable = r"don't\(\)"
x = re.sub(exp, repl, data)
x = x.split('\n')

for element in x:
    if re.findall(enable, element) != []:
        mnozi = True
    if re.findall(disable, element) != []:
        mnozi = False
    if mnozi:
        multiply = re.findall(exp, element)
        if multiply != []:
            brojevi = re.findall(r"[0-9]+", multiply[0])
            res = res + (int(brojevi[0])*int(brojevi[1]))
print(res)