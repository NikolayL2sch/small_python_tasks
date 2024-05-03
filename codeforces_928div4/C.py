t = int(input())

digits = [i for i in range(1, 47)]

for _ in range(t):
    n = int(input())
    cur_id = 0
    start_id = 0
    ans = 0
    len_n = 1
    for i in range(1, n + 1):
        if len_n + 1 == len(str(i)):
            ans += 1
            cur_id = 1
            len_n += 1
        elif i % 10 == 0:
            num_zeros = len(str(i)) - len(str(i).strip('0'))
            if num_zeros == 0:
                num_zeros = 1
            cur_id -= (8 + (num_zeros - 1) * 9)
            cur_id -= 1
            if cur_id < 0:
                cur_id = 0
            ans += digits[cur_id]
        elif len_n == len(str(i)):
            try:
                ans += digits[cur_id]
                cur_id += 1
            except:
                print(cur_id, i)

    print(ans)
