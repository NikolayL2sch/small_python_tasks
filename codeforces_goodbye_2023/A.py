t = int(input())

for i in range(t):
    flag_no = False
    n, k = map(int, input().split())
    b = [int(i) for i in input().split()]
    current = 2023
    for elem in b:
        if current % elem == 0:
            current = current // elem
        else:
            print("NO")
            flag_no = True
            break
    if not flag_no:
        if 2023 % current == 0:
            print("YES")
            print(current, end=' ')
            for _ in range(k - 1):
                print("1", end=' ')
            print()
