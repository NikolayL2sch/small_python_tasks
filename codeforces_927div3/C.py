import math

t = int(input())

for i in range(t):
    n, m = map(int, input().split())
    a = [int(i) for i in input().split()]
    s = input()

    # null_pos = [i for i in range(n) if a[i] % m == 0]

    l_pointer = 0
    r_pointer = n - 1

    pr = math.prod(a)

    prefix_product = [a[0] % m]  # Предпосчитывание префиксных произведений для ускорения вычислений
    for j in range(1, n):
        prefix_product.append((prefix_product[j - 1] * a[j]) % m)  # Произведение по модулю m

    for command in s:
        if command == 'L':
            print(pr % m, end=' ')
            pr //= a[l_pointer]
            l_pointer += 1
        elif command == 'R':
            print(pr % m, end=' ')
            pr //= a[r_pointer]
            r_pointer -= 1
    print()
