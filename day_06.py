#pt.1
with open('day_06.txt', 'r') as file_object:
    all_lines = file_object.readlines()
    instructions = []
    for line in all_lines:
        clean_line = line.strip()
        if clean_line:
            instructions.append(clean_line)

lit_lights = set()

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
            pos = (x, y)
            if action == 'on':
                lit_lights.add(pos)
            elif action == 'off':
                if pos in lit_lights:
                    lit_lights.remove(pos)
            elif action == 'toggle':
                if pos in lit_lights:
                    lit_lights.remove(pos)
                else:
                    lit_lights.add(pos)

print(len(lit_lights))

#pt.2
bright = {}

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
            pos = (x, y)
            curr = bright.get(pos, 0)
            if act == 'on':
                bright[pos] = curr + 1
            elif act == 'off':
                if curr - 1 >= 0:
                    bright[pos] = curr - 1
                else:
                    bright[pos] = 0
            elif act == 'toggle':
                bright[pos] = curr + 2

print(sum(bright.values()))
