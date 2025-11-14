import random

# 1. Створюємо список випадкової довжини від 3 до 10
lst = [random.randint(0, 9) for _ in range(random.randint(3, 10))]

# 2. Формуємо новий список: перший, третій і другий з кінця
result = [lst[0], lst[2], lst[-2]]

print(lst, "==", result)
