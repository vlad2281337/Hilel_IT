# 1. Квадрат числа
print("=== 1. Квадрат числа ===")
num = float(input("Введіть число: "))
print("Квадрат числа:", num ** 2)

# 2. Середнє трьох чисел
print("\n=== 2. Середнє трьох чисел ===")
a = float(input("Введіть перше число: "))
b = float(input("Введіть друге число: "))
c = float(input("Введіть третє число: "))
_average = (a + b + c) / 3
print("Середнє:", _average)

# 3. Перетворення хвилин у години
print("\n=== 3. Перетворення хвилин у години ===")
_minutes = int(input("Введіть кількість хвилин: "))
_hours = _minutes // 60
remaining_minutes = _minutes % 60
print(f"{_hours} годин {remaining_minutes} хвилин")

# 4. Розрахунок знижки
print("\n=== 4. Розрахунок знижки ===")
_price = float(input("Введіть ціну: "))
_discount = float(input("Введіть знижку (%): "))
final_price = _price - (_price * _discount / 100)
print("Ціна зі знижкою:", final_price)

# 5. Остання цифра числа
print("\n=== 5. Остання цифра числа ===")
_number = int(input("Введіть число: "))
last_digit = _number % 10
print("Остання цифра:", last_digit)

# 6. Периметр прямокутника
print("\n=== 6. Периметр прямокутника ===")
_length = float(input("Введіть довжину: "))
_width = float(input("Введіть ширину: "))
_perimeter = (_length + _width) * 2
print("Периметр:", _perimeter)

# 7. Виведення числа у стовпчик
print("=== 7. Виведення числа в стовпчик ===")

while True:
    try:
        num4 = int(input("Введіть 4-х значне число: "))
        if 1000 <= abs(num4) <= 9999:
            break
        else:
            print("Помилка: потрібно ввести саме 4-х значне число!")
    except ValueError:
        print("Помилка: введено не число!")

_num = abs(num4)
digit1 = _num // 1000
digit2 = (_num // 100) % 10
digit3 = (_num // 10) % 10
digit4 = _num % 10

print("Цифри числа:")
print(digit1)
print(digit2)
print(digit3)
print(digit4)
