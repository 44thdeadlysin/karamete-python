def count_types(items):
    result = {}
    for item in items:
        name = type(item).__name__
        if name in result:
            result[name] = result[name] + 1
        else:
            result[name] = 1
    return result
assert count_types([1, 'a', 2.5, True, 'b', 3]) == {'int': 2, 'str': 2, 'float': 1, 'bool': 1}
assert count_types([]) == {}