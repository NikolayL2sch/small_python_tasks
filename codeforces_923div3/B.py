t = int(input())
for i in range(t):
    letters = [0] * 26
    n = int(input())
    a = [int(i) for i in input().split()]
    for footprint in a:
        letter_id = letters.index(footprint)
        letters[letter_id] += 1
        print(chr(97 + letter_id), end='')
    print()
