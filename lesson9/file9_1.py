def popular_words(text, words):

    text = text.lower()

    text_words = text.split()

    result = {}
    for w in words:
        result[w] = text_words.count(w)

    return result


assert popular_words(
    '''When I was One I had just begun
       When I was Two I was nearly new ''',
    ['i', 'was', 'three', 'near']
) == {'i': 4, 'was': 3, 'three': 0, 'near': 0}, 'Test1'

print("OK, nad the rulust is :")

print(popular_words(
    '''When I was One I had just begun
       When I was Two I was nearly new ''',
    ['i', 'was', 'three', 'near']
))
