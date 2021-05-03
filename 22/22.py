def replace(maze, x, y, char):
    tempList = list(maze[x])
    tempList[y] = char
    maze[x] = tempList


def rec(maze: list, x, y):
    replace(maze, x, y, '!')
    if exits.__contains__(maze[x - 1][y]):
        print(maze[x - 1][y], end=" ")
    elif maze[x - 1][y] == ' ':
        rec(maze, x - 1, y)
    if exits.__contains__(maze[x + 1][y]):
        print(maze[x + 1][y], end=" ")
    elif maze[x + 1][y] == ' ':
        rec(maze, x + 1, y)
    if exits.__contains__(maze[x][y - 1]):
        print(maze[x][y - 1], end=" ")
    elif maze[x][y - 1] == ' ':
        rec(maze, x, y - 1)
    if exits.__contains__(maze[x][y + 1]):
        print(maze[x][y + 1], end=" ")
    elif maze[x][y + 1] == ' ':
        rec(maze, x, y + 1)


maze = [
    "####B######################",
    "# #       #   #      #    #",
    "# # # ###### #### ####### #",
    "# # # #       #   #       #",
    "#   # # ######### # ##### #",
    "# # # #   #       #     # #",
    "### ### ### ############# #",
    "# #   #     # #           #",
    "# # #   ####### ###########",
    "# # # #       # #         C",
    "# # ##### ### # # ####### #",
    "# # #     ### # #       # #",
    "#   ##### ### # ######### #",
    "######### ### #           #",
    "# ####### ### #############",
    "A           #   ###   #   #",
    "# ############# ### # # # #",
    "# ###       # # ### # # # #",
    "# ######### # # ### # # # F",
    "#       ### # #     # # # #",
    "# ######### # ##### # # # #",
    "# #######   #       #   # #",
    "# ####### ######### #######",
    "#         #########       #",
    "#######E############D######"
]
exits = ['A', 'B', 'C', 'D', 'F', 'E']
x, y = [int(i) for i in input().split()]

if x == 0 or y == 0 or x >= len(maze) or y >= len(maze[0]) or maze[x][y] == '#':
    print('Не верные координаты')
    exit()

rec(maze, x, y)
print()

for i in range(len(maze)):
    for j in range(len(maze[i])):
        if i == x and j == y:
            print('\033[94m' + "$" + '\033[0m', end=' ')
        elif maze[i][j] == '!':
            print('\033[92m' + "%" + '\033[0m', end=' ')
        else:
            print(maze[i][j], end=' ')
    print()
