counts = dict()

fhand = open('../Chapter 7/sample.txt')
x = fhand.read()
words = x.split()

for word in words:
    counts[word] = counts.get(word, 0) +1
print('Counts', counts)

""" Loop through dictionaries """

for key in counts:
    print(key, counts[key])

print(counts.keys())
print(counts.values())
print(counts.items())

for aaa, bbb in counts.items():
    print(aaa, bbb)