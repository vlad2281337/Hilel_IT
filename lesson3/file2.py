
lst = input("Введіть елементи списку через пробіл: ").split()

if len(lst) > 1:
    last = lst.pop()    
    lst.insert(0, last)

print("Новий список:", lst)
