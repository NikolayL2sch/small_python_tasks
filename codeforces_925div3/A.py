t = int(input())

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
           'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

for i in range(t):
    n = int(input())
    ans = []
    prev = []
    for j in range(3):
        if n >= 26:
            ans.append('z')
            n -= 26
            prev.append(25)
        elif n > 0:
            ans.append(letters[n - 1])
            prev.append(n - 1)
            n = 0
        else:
            if ans[-1] == 'a':
                ans.pop(0)
                ans.insert(0, letters[prev[0] - 1])
                ans.append('a')
            else:
                ans.pop()
                ans.append(letters[prev[-1] - 1])
                prev[-1] -= 1
                ans.append('a')
    ans.reverse()
    print(''.join(ans))