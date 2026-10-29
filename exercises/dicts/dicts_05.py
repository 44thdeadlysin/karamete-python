def count_letters(text):
    text = text.lower()
    result = {}
    for letter in text:
        letter = letter.strip(' ')
        if letter == '':
            continue
        elif letter in result:
            result[letter] = result[letter] + 1
        else:
            result[letter] = 1
    return result
assert count_letters("mama") == {"m": 2, "a": 2}
assert count_letters("cat cat") == {"c": 2, "a": 2, "t": 2}
assert count_letters("") == {}
print(count_letters("See Spot run"))