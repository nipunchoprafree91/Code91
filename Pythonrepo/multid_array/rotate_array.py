datas = [
    {"best": [5, 2, 9]},
    {"is":   [1, 4, 3]},
    {"of":   [8, 7, 6]}
]

output = [
    {"best": 5, "is": 2, "of": 9},
    {"best": 1, "is": 4, "of": 3},
    {"best": 8, "is": 7, "of": 6}
]

"""
Things to learn as part of this program.
1. Enumerate
2. dictionaries
3. Ordered dictionaries
"""

l1 = ["eat", "sleep", "repeat"]
print(list(enumerate(l1)))

l2 = "coding"
print(list(enumerate(l2)))

# changing index
print(list(enumerate(l2, 100)))
