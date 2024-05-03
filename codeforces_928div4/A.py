t = int(input())

for i in range(t):
    s = input()
    if s.count('A') > s.count('B'):
        print('A')
    else:
        print('B')
