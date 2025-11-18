
while True:
    print("\n--- Калькулятор ---")

    num1 = float(input("Введіть перше число: "))
    op = input("Введіть операцію (+, -, *, /): ")
    num2 = float(input("Введіть друге число: "))

    if op == "+":
        print("Результат:", num1 + num2)
    elif op == "-":
        print("Результат:", num1 - num2)
    elif op == "*":
        print("Результат:", num1 * num2)
    elif op == "/":
        if num2 == 0:
            print("Ділення на нуль неможливе!")
        else:
            print("Результат:", num1 / num2)
    else:
        print("Помилка! Невірна операція.")

    again = input("\nБажаєте продовжити? (y/yes для продовження): ").lower()

    if again not in ("y", "yes"):
        print("Програма завершена. До побачення!")
        break
