inventory = ['potion', 'potion']
item = input('Item to remove: ')
if item in inventory:
    inventory.remove(item)
    print('Removed:', item)
else:
    print('Item not found')
print(inventory)