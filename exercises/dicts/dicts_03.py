words = ["cat", "dog", "cat", "bird", "cat", "dog"]
counts = {}
for word in words:
    if word in counts:
        counts[word] = counts[word] + 1
    else:
        counts[word] = 1
print(counts)