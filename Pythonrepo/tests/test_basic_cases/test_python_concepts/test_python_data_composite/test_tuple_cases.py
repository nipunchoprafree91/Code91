tuples = [(1, 'one'), (3, 'three'), (2, 'two')]
tuples.sort(key=lambda x: x[1])
print(tuples)

a = [1, 2, 3, 4] # list 1
b = [ 5, 6, 7, 8, 9] # list 2
a.extend(b)
print(a)

a = [1, 2, 3, 4] # list 1
b = [ 5, 6, 7, 8, 9] # list 2
a.append(b)
print(a)

# Compare this snippet from tests/test_basic_cases/test_python_concepts/test_list_cases.py: