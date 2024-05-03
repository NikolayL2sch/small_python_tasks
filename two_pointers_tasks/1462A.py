t = int(input())
for i in range(t):
    n = int(input())
    b = list(map(int, input().split()))
    a = []
    left = 0
    right = n - 1
    move = 0
    while left <= right:
        if move % 2 == 0:
            a.append(b[left])
            left += 1
        else:
            a.append(b[right])
            right -= 1
        move += 1
    print(*a)
