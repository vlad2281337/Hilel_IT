def get_day_word(n):

    if n % 10 == 1 and n % 100 != 1:
        return "день"
    elif n % 10 in (2, 3, 4) and not (12 <= n % 100 <= 14):
        return "дні"
    else:
        return "днів"


print("Введіть кількість секунд (0–8639999) або 'stop' для виходу:")

while True:
    user_input = input("> ").replace(" ", "")

    if user_input.lower() in ("stop", "exit"):
        print("Програма завершена.")
        break

    if not user_input.isdigit():
        print("Помилка: введіть невід’ємне число секунд.")
        continue

    seconds = int(user_input)

    if not (0 <= seconds < 8640000):
        print("Помилка: число повинно бути в межах 0–8639999.")
        continue

    days, remainder = divmod(seconds, 24 * 3600)
    hours, remainder = divmod(remainder, 3600)
    minutes, sec = divmod(remainder, 60)

    h = str(hours).zfill(2)
    m = str(minutes).zfill(2)
    s = str(sec).zfill(2)

    day_word = get_day_word(days)

    print(f"{days} {day_word}, {h}:{m}:{s}")
