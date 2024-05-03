s = input()
a = [ord(elem) for elem in s]
max_id = []
min_id = []
max_elem = max(a)
min_elem = min(a)

ans_start = 0
ans_end = 0

for i in range(len(s)):
    if a[i] == min_elem:
        min_id.append(i)
    elif a[i] == max_elem:
        max_id.append(i)

max_diff = 0

for i in range(len(min_id)):
    for j in range(len(max_id)):
        if abs(a[min_id[i]] - a[max_id[j]]) > max_diff:
            max_diff = abs(a[min_id[i]] - a[max_id[j]])
            ans_start = min(min_id[i], max_id[j])
            ans_end = max(min_id[i], max_id[j])
        elif abs(a[min_id[i]] - a[max_id[j]]) == max_diff and abs(min_id[i] - max_id[j]) < abs(ans_start - ans_end):
            ans_start = min(min_id[i], max_id[j])
            ans_end = max(min_id[i], max_id[j])

print(s[ans_start:ans_end + 1:])