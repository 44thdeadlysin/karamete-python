def parse_numbers(numbers):
    numbers = numbers.split()
    results = []
    for x in numbers:
        x = int(x)
        results.append(x)
    return results
assert parse_numbers('70 55 90') == [70, 55, 90]
assert parse_numbers('') == []
assert parse_numbers(' 1   2 ') == [1, 2]