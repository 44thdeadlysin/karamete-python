def remove_duplicate(text):
    text = text.lower()
    text = text.split()
    words = []
    repeat_count = 0
    for word in text:
        word = word.strip('.,!?')
        if word == (''):
            continue
        elif word in words:
            repeat_count = repeat_count + 1
        else:
            words.append(word)
    return words, repeat_count
assert remove_duplicate('potion potion potion') == (['potion'],2)
assert remove_duplicate('!!! sword') == (['sword'], 0)
assert remove_duplicate('potion Potion sword') == (['potion', 'sword'],1)
assert remove_duplicate('') == ([], 0)

text = input('Input your items: ')
words, repeat_count = remove_duplicate(text)
print('Unique items: ' + ', '.join(words))
print('Repeat count: ' + str(repeat_count))