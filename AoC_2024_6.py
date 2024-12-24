data_split = []

with open('AoC_2024_6.txt', 'r') as file:
    data = file.read()

start = data.find('^')
row_length = data.find('\n')
column_length = data.count('\n')
current_move = start

i = 0
up = -row_length-1
down = row_length+1
left = -1 
right = 1
max = row_length*column_length
orientations = ['up', 'right', 'down', 'left']
start_orientation = orientations[i]
current_orientation = start_orientation
last_move = 0
counter = 1

def move(current, current_orientation, i, last_move):
    if data.find("#", current) == current:
        i = (i + 1) % 4
        current = current - last_move
        current_orientation = orientations[i]
    if current_orientation == 'up':
        last_move = up
        current = current + up
    if current_orientation == 'down':
        last_move = down
        current = current + down
    if current_orientation == 'left':
        last_move = left
        current = current + left
    if current_orientation == 'right':
        last_move = right
        current = current + right
    return current, current_orientation, i, last_move

def mark_trail(data, current):
    if data[current] != ('#') :
        data = data[: current] + 'X' + data[current + 1:]
    return data

while 0 < current_move < max:
    next_move, current_orientation, i, last_move = move(current_move, current_orientation, i, last_move)
    data = mark_trail(data, current_move)
    current_move = next_move
    if data[current_move] == '\n':
        break
print(data.count('X'))
