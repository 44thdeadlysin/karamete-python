counts = {"cat": 3, "dog": 1}
question = input('Enter an animal:')
if question in counts:
    print('Animal found')
else:
    print('Animal not found')
