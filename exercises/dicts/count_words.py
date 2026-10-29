def count_words(text):
    text = text.lower()
    text = text.split()
    result = {}
    for word in text:
        word = word.strip(".,!?")
        if word == '':
            continue
        elif word in result:
            result[word] = result[word] + 1
        else:
            result[word] = 1
    return result
assert count_words("cat cat") == {"cat": 2}
assert count_words('Cat cat!') == {'cat': 2}
assert count_words('!!! ...') == {}
print(count_words('Cat cat cat'))