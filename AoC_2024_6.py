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
counter = 1

def move(current):
    if data.find("#", current) == current:
        return current
    if current_orientation == 'up':
        current = current + up
    if current_orientation == 'down':
        current = current + down
    if current_orientation == 'left':
        current = current + left
    if current_orientation == 'right':
        current = current + right
    return current


while 0 < current_move < max:
    next_move = move(current_move)
    if next_move == current_move:
        current_orientation = orientations[i+1]
        break
