n, m = map(int, input().split())

c = int(input())
s = input()

mat = [[[False for j in range(4)] for i in range((m + 1))] for _ in range((n + 1))]
total_len = 0
cur_len = 1
prev_move = ''
x, y = 0, 0
for move in s:
    if move != prev_move:
        total_len += cur_len
        cur_len = 1
    else:
        cur_len += 1
    if move == 'U':
        mat[x][y][0] = True
        y += 1
        if mat[x][y][1]:
            cur_len -= 1
        mat[x][y][1] = True
    elif move == 'D':
        mat[x][y][1] = True
        y -= 1
        if mat[x][y][0]:
            cur_len -= 1
        mat[x][y][0] = True
    elif move == 'R':
        mat[x][y][2] = True
        x += 1
        if mat[x][y][3]:
            cur_len -= 1
        mat[x][y][3] = True
    elif move == 'L':
        mat[x][y][3] = True
        x -= 1
        if mat[x][y][2]:
            cur_len -= 1
        mat[x][y][2] = True
    prev_move = move

print(total_len)
