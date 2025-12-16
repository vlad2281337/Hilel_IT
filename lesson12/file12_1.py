import codecs

def delete_html_tags(html_file, result_file='cleaned.txt', remove_empty_lines=True):
    with codecs.open(html_file, 'r', 'utf-8') as f:
        html = f.read()

    result = []
    in_tag = False

    for ch in html:
        if ch == '<':
            in_tag = True
            continue
        if ch == '>' and in_tag:
            in_tag = False
            continue
        if not in_tag:
            result.append(ch)

    text = ''.join(result)

    if remove_empty_lines:
        lines = [line.strip() for line in text.splitlines()]
        lines = [line for line in lines if line]
        text = '\n'.join(lines)

    with codecs.open(result_file, 'w', 'utf-8') as f:
        f.write(text)


# 🔽 ОБОВʼЯЗКОВО додати
delete_html_tags('draft.html')
