t = int(input())

for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    amount = sum(a) // n
    flag = True
    for j in range(n - 1):
        if a[j] > amount:
            a[j + 1] += a[j] - amount
            a[j] = amount
        elif a[j] < amount:
            flag = False
            break

    if not flag or a[-1] != amount:
        print("NO")
    else:
        print("YES")
