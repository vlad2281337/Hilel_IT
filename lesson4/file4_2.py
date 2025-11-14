def sum_even_index_mult_last(lst):
    if not lst:
        return 0

    even_sum = sum(lst[i] for i in range(0, len(lst), 2))
    return even_sum * lst[-1]

print(sum_even_index_mult_last([0, 1, 7, 2, 4, 8]))
print(sum_even_index_mult_last([1, 3, 5]))
print(sum_even_index_mult_last([6]))
print(sum_even_index_mult_last([]))
