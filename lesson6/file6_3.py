def multiply_digits(num):
    result = 1
    for d in str(num):
        result *= int(d)
    return result


print("Введіть ціле число (або 'stop' для виходу):")

while True:
    user_input = input("> ").replace(" ", "")

    if user_input.lower() in ("stop", "exit"):
        print("Програма завершена.")
        break

    if not user_input.lstrip("-").isdigit():
        print("Помилка: введіть ціле число.")
        continue

    n = abs(int(user_input))

    while n > 9:
        n = multiply_digits(n)

    print(n)
