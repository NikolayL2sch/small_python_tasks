def find_longest_sequence(arr):
    max_ans_1 = 1
    cur_ans = 1
    max_num_1 = -1
    cur_num = -1
    max_ans_2 = 1
    max_num_2 = -2
    for _ in range(1, len(arr)):
        if arr[_] == arr[_ - 1]:
            cur_ans += 1
            cur_num = arr[_]
        else:
            max_num_1 = arr[0]
            break
        if cur_ans > max_ans_1:
            max_ans_1 = cur_ans
            max_num_1 = cur_num

    cur_ans = 1

    for _ in range(len(arr) - 1, -1, -1):
        if arr[_ - 1] == arr[_]:
            cur_ans += 1
            cur_num = arr[_]
        else:
            max_num_2 = arr[-1]
            break
        if cur_ans > max_ans_2:
            max_ans_2 = cur_ans
            max_num_2 = cur_num
    if max_num_1 == max_num_2:
        return n - max_ans_1 - max_ans_2 if n - max_ans_1 - max_ans_2 >= 0 else 0
    return n - max(max_ans_1, max_ans_2) if n - max(max_ans_1, max_ans_2) >= 0 else 0


t = int(input())

for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    print(find_longest_sequence(a))