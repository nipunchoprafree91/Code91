original_dict = {"best": 5, "is": 2, "of": 9}

for key, val in original_dict.items():
    print(key, val)

# Dict domprehensions
original_dict = {"best": 5, "is": 2, "of": 9}

new_dict = {key: value for key, value in original_dict.
            items() if value % 2 == 0}
print(new_dict)

pairs = [('a', 1), ('b', 2), ('c', 3)]
new_dict2 = {key: value for key,
             value in pairs if value % 2 == 0}
print(new_dict2)
