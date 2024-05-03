def distance(x1, y1, x2, y2):
    return (x2 - x1)**2 + (y2 - y1)**2


t = int(input())

for i in range(t):
    flag = False
    v = [[int(k) for k in input().split()]]
    for j in range(3):
        point = [int(i) for i in input().split()]
        if point[0] != v[0][0] and point[1] != v[0][1] and not flag:
            print(int(distance(point[0], point[1], v[0][0], v[0][1]) / 2))
            flag = True
