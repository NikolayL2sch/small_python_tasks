t = int(input())

for i in range(t):
    n = int(input())
    s = input()
    f = input()
    cnt = 0
    for _ in range(n):
        if s[_] != f[_]:
            cnt += 1
    print((abs(s.count('1') - f.count('1')) + cnt) // 2)