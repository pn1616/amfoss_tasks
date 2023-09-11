s = input()

indices = [0, 0, 0, 0, 0]

for char in s:
    if char == "h" and indices[0] == 0:
        indices[0] = 1
    elif char == "e" and indices[0] == 1 and indices[1] == 0:
        indices[1] = 1
    elif char == "l" and indices[1] == 1 and (indices[2] == 0 or indices[3] == 1):
        indices[2] = 1
    elif char == "l" and indices[2] == 1 and indices[3] == 0:
        indices[3] = 1
    elif char == "o" and indices[3] == 1 and indices[4] == 0:
        indices[4] = 1

if all(index == 1 for index in indices):
    print("YES")
else:
    print("NO")
