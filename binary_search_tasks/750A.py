n, k = map(int, input().split())
time_left = 240 - k
cnt = 0
for i in range(1, n + 1):
    if time_left - 5 * i >= 0:
        time_left -= 5 * i
        cnt += 1
    else:
        break
print(cnt)
