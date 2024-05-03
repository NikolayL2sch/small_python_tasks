t = int(input())

for i in range(t):
    n = int(input())
    s = input()
    ans = -1
    for j in range(n - 1):
        if s[j] == '*' and s[j + 1] == '*':
            ans = s[:j:].count('@')
            break
    if ans == -1:
        ans = s.count('@')
    print(ans)
