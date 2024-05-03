t = int(input())
for i in range(t):
    n = int(input())
    a = [int(i) for i in input().split()]
    if int(sum(a) ** 0.5) ** 2 == sum(a):
        print("YES")
    else:
        print("NO")
