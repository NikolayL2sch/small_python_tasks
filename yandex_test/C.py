s = input()
a = [ord(elem) for elem in s]

max_diff_s = 0
max_id_s = 0
max_id_e = 0
for i in range(len(s) - 1):
    max_diff = abs(a[i] - a[i + 1])
    if a[i] < a[i + 1]:
        min_el = a[i]
        min_id = i
        max_el = a[i + 1]
        max_id = i + 1
    else:
        min_el = a[i + 1]
        min_id = i + 1
        max_el = a[i]
        max_id = i
    for j in range(i + 2, len(s)):
        if a[j] < a[min_id]:
            min_el = a[j]
            min_id = j
            max_diff = abs(a[max_id] - a[min_id])
        elif a[j] > a[max_id]:
            max_el = a[j]
            max_id = j
            max_diff = abs(a[max_id] - a[min_id])
    if max_diff_s < max_diff:
        max_diff_s = max_diff
        max_id_s = min(min_id, max_id)
        max_id_e = max(min_id, max_id)
    elif max_diff_s == max_diff and abs(max_id - min_id) < max_id_e - max_id_s:
        max_id_s = min_id
        max_id_e = max_id
print(s[max_id_s:max_id_e + 1:])
