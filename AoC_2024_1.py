#!/usr/bin/python3

f = open("AoC_2024_1.txt","r")
lists = f.readlines()
list1 = []
list2 = []
sim_score = 0

for x in lists:
    x = x.split('   ')
    list1.append(int(x[0]))
    list2.append(int(x[1]))

for i in list1:
    for j in list2:
        if j == i:
            sim_score = sim_score + j

print(sim_score)
    
    
