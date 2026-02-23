#pt.1
with open('day_03.txt', 'r') as file_object:
    input_text = file_object.read()

pos = (0,0)
visited = set()
visited.add(pos)

for char in input_text:
    x,y = pos
    if char == '>':
        x = x + 1
    elif char == '<':
        x = x - 1
    elif char == '^':
        y = y + 1
    elif char == 'v':
        y = y - 1
    pos = (x,y)
    visited.add(pos)

print(len(visited))

#pt.2
santa_x, santa_y = 0,0
robo_x, robo_y = 0,0
two_visited = set()
two_visited.add((0,0))

if input_text:
    for step, char in enumerate(input_text, start=1):
        if step % 2 == 1:
            if char == '>':
                santa_x = santa_x + 1
            elif char == '<':
                santa_x = santa_x - 1
            elif char == '^':
                santa_y = santa_y + 1
            elif char == 'v':
                santa_y = santa_y - 1
            two_visited.add((santa_x, santa_y))
        else:
            if char == '>':
                robo_x = robo_x + 1
            elif char == '<':
                robo_x = robo_x - 1
            elif char == '^':
                robo_y = robo_y + 1
            elif char == 'v':
                robo_y = robo_y - 1
            two_visited.add((robo_x, robo_y))

print(len(two_visited))
