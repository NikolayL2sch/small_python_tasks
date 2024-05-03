t = int(input())

for i in range(t):
    n = int(input())
    s = input()
    min_black = -1
    max_black = -1
    for j in range(len(s)):
        if s[j] == 'B':
            if min_black == -1:
                min_black = j
            else:
                max_black = j
    if min_black == -1:
        print(0)
    elif min_black != -1 and max_black == -1:
        print(1)
    else:
        print(max_black - min_black + 1)