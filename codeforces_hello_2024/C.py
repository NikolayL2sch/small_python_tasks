t = int(input())
for i in range(t):
    n, f, a, b = map(int, input().split())
    m = [int(_) for _ in input().split()]
    flag = True
    if n > 1:
        m_d = [m[0]]
        m_d.extend([m[_ + 1] - m[_] for _ in range(n - 1)])
    else:
        m_d = m
    for _ in m_d:
        if _ * a <= b:
            f -= _ * a
        else:
            f -= b
        if f <= 0:
            print("NO")
            flag = False
            break
    if flag:
        print("YES")