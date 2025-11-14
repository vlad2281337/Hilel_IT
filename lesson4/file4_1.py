def move_zeros(lst):
    result = []
    zero_count = 0

    for x in lst:
        if x == 0:
            zero_count += 1
        else:
            result.append(x)

    result.extend([0] * zero_count)
    return result


print(move_zeros([0, 1, 0, 12, 3]))
print(move_zeros([0]))
print(move_zeros([1, 0, 13, 0, 0, 0, 5]))
print(move_zeros([9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]))
