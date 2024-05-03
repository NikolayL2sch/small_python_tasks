def sum_of_numbers_on_board(n):
    total_sum = 0
    for i in range(1, n + 1):
        digit_sum = i // 1000 + (i % 1000) // 100 + (i % 100) // 10 + i % 10
        total_sum += digit_sum
    return total_sum

n = 12
result = sum_of_numbers_on_board(n)
print(f"Сумма чисел на доске после замены: {result}")