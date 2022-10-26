room_map = [[1,1,1,1,1],
            [1,0,0,0,1],
            [1,0,1,0,1],
            [1,0,0,0,1],
            [1,0,0,0,1],
            [1,0,0,0,1],
            [1,1,1,1,1]]

for y in range(7):
    for x in range(5):
        print(room_map[y][x], end="") # (end="") tells program to not create new line between each print
    print()