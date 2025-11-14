def sum_even_index_mult_last(lst):
    if not lst:          # якщо список порожній → результат 0
        return 0

    # сума елементів з парними індексами
    even_sum = sum(lst[i] for i in range(0, len(lst), 2))

    # множимо на останній елемент
    return even_sum * lst[-1]

print(sum_even_index_mult_last([0, 1, 7, 2, 4, 8]))  # 88
print(sum_even_index_mult_last([1, 3, 5]))           # 30
print(sum_even_index_mult_last([6]))                 # 36
print(sum_even_index_mult_last([]))                  # 0
