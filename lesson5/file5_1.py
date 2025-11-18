
import string
import keyword

def is_valid_variable(name: str) -> bool:

    if not name:
        return False
    if name[0].isdigit():
        return False

    allowed_chars = set("abcdefghijklmnopqrstuvwxyz0123456789_")

    forbidden_punct = set(string.punctuation.replace("_", ""))

    for ch in name:
        if ch in forbidden_punct:
            return False
        if ch == " ":
            return False
        if ch.isalpha() and ch.isupper():
            return False
        if ch not in allowed_chars:
            return False

    if name.count("_") > 1:
        return False

    if name in keyword.kwlist:
        return False

    return True

tests = ["_", "__", "___", "x", "get_value", "get value", "get!value",
         "some_super_puper_value", "Get_value", "get_Value",
         "getValue", "3m", "m3", "assert", "assert_exception"]

for t in tests:
    print(t, "=>", is_valid_variable(t))
