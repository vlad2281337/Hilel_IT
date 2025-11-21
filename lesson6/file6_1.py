import string

def letters_range(text: str) -> str:
    # Прибираємо всі пробіли
    text = text.replace(" ", "")

    if text.count('-') != 1:
        return "Помилка: введіть у форматі літера-літера, наприклад a-c"

    start, end = text.split('-')

    if len(start) != 1 or len(end) != 1:
        return "Помилка: введіть по одній літері з кожного боку дефісу."

    letters = string.ascii_letters

    if start not in letters or end not in letters:
        return "Помилка: дозволені тільки англійські літери."

    i1 = letters.index(start)
    i2 = letters.index(end)

    return letters[i1:i2+1]

while True:
    user_input = input("Введіть дві літери через дефіс (або 'stop' для виходу): ")

    if user_input.replace(" ", "").lower() in ("stop", "exit"):
        print("Програма завершена.")
        break

    result = letters_range(user_input)
    print(result)
