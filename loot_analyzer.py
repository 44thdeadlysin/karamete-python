def count_loot(text):
    text = text.lower()
    text = text.split()
    loot = {}
    for word in text:
        word = word.strip('.,!?')
        if word == '':
            continue
        elif word in loot:
            loot[word] = loot[word] + 1
        else:
            loot[word] = 1
    return loot

assert count_loot('sword sword potion') == {'sword': 2, 'potion': 1}
assert count_loot('SWORD, sword!') == {'sword': 2}
assert count_loot('!!!') == {}
assert count_loot('') == {}
assert count_loot('SWORD, sword! shield key') == {
    'sword': 2,
    'shield': 1,
    'key': 1
}
assert count_loot('!!! ...') == {}

loot = input('Enter loot: ')
loot = count_loot(loot)
total_items = 0
for item in loot:
    total_items = total_items + loot[item]
different_items = len(loot)
single_items = []
for item in loot:
    if loot[item] == 1:
        single_items.append(item)

print('Total items:', total_items)
print('Different items:', different_items)
print('Single items:', single_items)