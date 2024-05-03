import math

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    a = [int(i) for i in input().split()]
    s = input()

    pr = math.prod(a)
    prefix_product = [1] * (n + 1)  # Предпосчитывание префиксных произведений для ускорения вычислений
    for i in range(n):
        prefix_product[i + 1] = (prefix_product[i] * a[i]) % m  # Произведение по модулю m

    l_pointer = 0
    r_pointer = n

    for command in s:
        if command == 'L':
            print(prefix_product[r_pointer] * pr // prefix_product[l_pointer + 1] % m, end=' ')
            l_pointer += 1
        elif command == 'R':
            print(prefix_product[r_pointer - 1] * pr // prefix_product[l_pointer] % m, end=' ')
            r_pointer -= 1
    print()
