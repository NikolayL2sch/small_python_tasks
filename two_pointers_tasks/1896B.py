t = int(input())
for i in range(t):
    n = int(input())
    s = input()
    operations = 0
    last_B = s.rfind('B')
    first_A = s.find('A')
    if last_B == -1 or first_A == -1 or last_B - first_A < 0:
        print(0)
    else:
        print(last_B - first_A)
