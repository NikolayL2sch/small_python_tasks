t = int(input())

for i in range(t):
    n = int(input())
    field = []
    str_id = 1
    for _ in range(n):
        field.append(input())

    for _ in range(n - 1):
        if field[_].count('1') > 0:
            if field[_].count('1') == field[_ + 1].count('1'):
                print("SQUARE")
            else:
                print("TRIANGLE")
            break
