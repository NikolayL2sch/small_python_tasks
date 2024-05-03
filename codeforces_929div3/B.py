t = int(input())

for i in range(t):
    n = int(input())
    a = [int(i) % 3 for i in input().split()]
    ans = sum(a) % 3
    if ans == 0:
        print(0)
    else:
        if ans not in a:
            print(3 - ans)
        else:
            print(1)
