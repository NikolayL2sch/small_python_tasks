def num_left(arr):
    chet = [elem for elem in arr if elem % 2 == 0]
    nechet = [elem for elem in arr if elem % 2 == 1]
    while len(chet) + len(nechet) > 1:
        if len(nechet) == 0:
            return [sum(chet)]
        if len(nechet) >= 2:
            chet.append(nechet[-1] + nechet[-2])
            nechet.pop()
            nechet.pop()
        elif len(chet) >= 2:
            res = chet[-1] + chet[-2]
            chet.pop()
            chet.pop()
            chet.append(res)
        else:
            res = int((nechet[-1] + chet[-1]) / 2) * 2
            nechet.pop()
            chet.pop()
            chet.append(res)
        if len(chet) >= 1 and len(nechet) >= 1:
            res = int((nechet[-1] + chet[-1]) / 2) * 2
            nechet.pop()
            chet.pop()
            chet.append(res)
        elif len(nechet) >= 2:
            res = nechet[-1] + nechet[-2]
            nechet.pop()
            nechet.pop()
            chet.append(res)
        elif len(chet) >= 2:
            res = chet[-1] + chet[-2]
            chet.pop()
            chet.pop()
            chet.append(res)
    return chet + nechet


t = int(input())
for i in range(t):
    n = int(input())
    a = [int(i) for i in input().split()]
    for j in range(1, n + 1):
        print(*num_left(a[:j:]), end=' ')
    print()
