import string

def make_hashtag(text: str) -> str:
    cleaned = ""
    for ch in text:
        if ch not in string.punctuation and not ch.isspace():
            cleaned += ch

    tmp = text
    for p in string.punctuation:
        tmp = tmp.replace(p, " ")
    words = tmp.split()

    words = [w.capitalize() for w in words]

    hashtag = "#" + "".join(words)

    if len(hashtag) > 140:
        hashtag = hashtag[:140]

    return hashtag


print(make_hashtag('Python Community'))
print(make_hashtag('i like python community!'))
print(make_hashtag('Should, I. subscribe? Yes!'))
