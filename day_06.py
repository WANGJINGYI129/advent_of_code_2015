#pt.1
with open('day_06.txt', 'r') as file_object:
    all_lines = file_object.readlines()
    instructions = []
    for line in all_lines:
        clean_line = line.strip()
        if clean_line:
            instructions.append(clean_line)

light_switch = [[False for _ in range(1000)] for _ in range(1000)]

for char in instructions:
    words = char.split()
    if words[0] == 'turn': #'turn' 'on' '887,9' 'through' '959,629'
        action = words[1]
        x1, y1 = map(int, words[2].split(','))
        x2, y2 = map(int, words[4].split(','))
    elif words[0] == 'toggle': #'toggle' '720,196' 'through' '897,994'
        action = 'toggle'
        x1, y1 = map(int, words[1].split(','))
        x2, y2 = map(int, words[3].split(','))
    else:
        continue

    for x in range(x1, x2 + 1):
        for y in range(y1, y2 + 1):
            if action == 'on':
                light_switch[x][y] = True
            elif action == 'off':
                light_switch[x][y] = False
            elif action == 'toggle':
                light_switch[x][y] = not light_switch[x][y]

lit_count = 0
for i in light_switch:
    lit_count = lit_count + i.count(True)
print(lit_count)

#pt.2
light_bright = [[0 for _ in range(1000)] for _ in range(1000)]

for char in instructions:
    words = char.split()
    if words[0] == 'turn':
        act = words[1]
        x1, y1 = map(int, words[2].split(','))
        x2, y2 = map(int, words[4].split(','))
    elif words[0] == 'toggle':
        act = 'toggle'
        x1, y1 = map(int, words[1].split(','))
        x2, y2 = map(int, words[3].split(','))

    for x in range(x1, x2 + 1):
        for y in range(y1, y2 + 1):
            curr = light_bright[x][y]
            if act == 'on':
                light_bright[x][y] = curr + 1
            elif act == 'off':
                if curr - 1 >= 0:
                    light_bright[x][y] = curr - 1
                else:
                    light_bright[x][y] = 0
            elif act == 'toggle':
                light_bright[x][y] = curr + 2

total_bright = 0
for row in light_bright:
    total_bright += sum(row)
print(total_bright)
