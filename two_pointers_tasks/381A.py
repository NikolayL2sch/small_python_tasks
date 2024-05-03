n = int(input())
a = [int(i) for i in input().split()]
i = 0
j = n - 1
s_sum = 0
d_sum = 0
move = 0
while i <= j:
    if a[i] > a[j]:
        if move % 2 == 0:
            s_sum += a[i]
        else:
            d_sum += a[i]
        i += 1
    else:
        if move % 2 == 0:
            s_sum += a[j]
        else:
            d_sum += a[j]
        j -= 1
    move += 1

print(s_sum, d_sum)