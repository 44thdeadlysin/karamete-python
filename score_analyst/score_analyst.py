def analysis(scores):
    score = sorted(scores)
    return score[-1], score[0], sum(score)/len(score)
assert analysis([70, 55, 90, 85, 60]) == (90, 55, 72)
assert analysis([1]) == (1, 1, 1)
assert analysis([1, 2, 4]) == (4, 1, 7/3)
def top_three(scores):
    scores = sorted(scores)
    scores = scores[::-1]
    return scores[0:3]
assert top_three([70, 55, 90, 85, 60]) == [90, 85, 70]
assert top_three([1]) == [1]
assert top_three([1, 2, 4]) == [4, 2, 1]
marks = [70, 55, 90, 85, 60]
original = marks.copy()
top_three(marks)
assert marks == original
def median(scores):
    scores = sorted(scores)
    mid = len(scores) // 2
    if len(scores) % 2 == 1:
        return scores[mid]
    return (scores[mid - 1] + scores[mid]) / 2
assert median([70, 55, 90, 85, 60]) == 70
assert median([1, 2, 4, 10]) == 3.0
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
user_marks = input('Input your marks: ')
if user_marks == '':
     print('List is empty.')
else:
    scores = parse_numbers(user_marks)
    best, worst, average = analysis(scores)
    print('Best mark:', best)
    print('Worst mark:', worst)
    print('Average mark:', average)
    print('Top three:', top_three(scores))
    print('Median:', median(scores))