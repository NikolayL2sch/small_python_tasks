t = int(input())
for i in range(t):
    n, m, k = map(int, input().split())
    a = set([int(i) for i in input().split()])
    b = set([int(i) for i in input().split()])
    if len(a) < k // 2 or len(b) < k // 2:
        print("NO")
    else:
        used_1 = 0
        used_2 = 0
        both = 0
        for j in range(1, k):
            if j in a and j in b:
                both += 1
                used_1 += 1
            elif j in a:
                used_1 += 1
            elif j in b:
                used_2 += 1
        if used_1 > k // 2:
            if used_1 - both <= k // 2:
                print("YES")
            else:
                print("NO")
        elif used_2 > k // 2:
            print("NO")
        else:
            print("YES")