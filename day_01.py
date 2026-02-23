#pt.1
with open('day_01.txt', 'r') as file_object:
    input_text = file_object.read()

final_floor = 0

for char in input_text:
    if char == '(':
        final_floor = final_floor + 1
    elif char == ')':
        final_floor = final_floor - 1
print(final_floor)

#pt.2
current_floor = 0
basement_position = 0

for position, char in enumerate(input_text, start=1):
    if char == '(':
        current_floor = current_floor + 1
    elif char == ')':
        current_floor = current_floor - 1

    if current_floor == -1 and basement_position == 0:
        basement_position = position
        break
print(basement_position)