t = int(input())

for i in range(t):
    a, b, l = map(int, input().split())
    x_count = 1
    y_count = 1
    num = l
    while num % a == 0:
        x_count += 1
        num //= a
    num = l
    while num % b == 0:
        y_count += 1
        num //= b
    print(x_count * y_count)