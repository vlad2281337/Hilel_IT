
lst = input("Введіть елементи списку через пробіл: ").split()

if len(lst) == 0:
    new_list = [[], []]
else:
    middle = (len(lst) + 1) // 2
    first_half = lst[:middle]
    second_half = lst[middle:]
    new_list = [first_half, second_half]

print("Новий список із двох списків:", new_list)
