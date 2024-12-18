import numpy as np
input = np.loadtxt("AoC_2024_4.txt", dtype='str', delimiter=',')

input_split = []
for element in input:
    row = list(element)
    input_split.append(row)

counter_1 = 0
counter_2 = 0
lista_1 = []
lista_2 = []
lista_1_2 = []
lista_2_2 = []
target_fw = ['X','M','A','S']
target_bw = ['S','A','M','X']
target_fw_2 = ['S', 'A', 'M']
target_bw_2 = ['M', 'A', 'S']
shape = np.shape(input_split)
input_split_t = np.transpose(input_split)
for j in range(shape[0]):
    for i in range(shape[1]):
        if (list(input_split[j][i:i+4]) == target_fw or list(input_split[j][i:i+4]) == target_bw):
            counter_1 += 1
        if (list(input_split_t[j][i:i+4]) == target_fw or list(input_split_t[j][i:i+4]) == target_bw):
            counter_1 += 1
        for x in range(4):
            if i < 137 and j < 137:
                lista_1.append(input_split[j+x][i+x])
            if i < 137 and j > 2:
                lista_2.append(input_split[j-x][i+x])

        if i < 138 and j < 138:
            for x in range(3):
                lista_1_2.append(input_split[j+x][i+x])
                lista_2_2.append(input_split[j-x+2][i+x])

        if (lista_1 == target_fw or lista_1 == target_bw):
            counter_1 += 1
        if (lista_2 == target_fw or lista_2 == target_bw):
            counter_1 += 1
        
        if ((lista_1_2 == target_fw_2 or lista_1_2 == target_bw_2) and
            (lista_2_2 == target_fw_2 or lista_2_2 == target_bw_2)):
            counter_2 += 1
        lista_1 = []
        lista_2 = []
        lista_1_2 = []
        lista_2_2 = []

print(counter_1)
print(counter_2)
