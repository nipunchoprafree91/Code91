pairs = [('a', 1), ('b', 2), ('c', 3)]
for i, j in pairs:
    print(i, j)

# create a list of tuples with student
# details
name = [('sravan', 7058, 98.45),
        ('ojaswi', 7059, 90.67),
        ('bobby', 7060, 78.90),
        ('rohith', 7081, 67.89),
        ('gnanesh', 7084, 98.01)]

# iterate using for loop
for x in name:
    # iterate in each tuple element
    for y in x:
        print(y)
    print()

# create a list of tuples with student
# details
name = [('sravan', 7058, 98.45),
        ('ojaswi', 7059, 90.67),
        ('bobby', 7060, 78.90),
        ('rohith', 7081, 67.89),
        ('gnanesh', 7084, 98.01)]
list1 = []

# iterate using index with enumerate function
for index, tuple in enumerate(name):
    # access through index
    # by appending to list
    list1.append(name[index])

print()
print("value of  l is :{}".format(list1))
print()

# iterate through the list
for x in list1:
    for y in x:
        print(y)
    print()

for name, roll, perc in [['sravan', 7058, 98.45]]:
    print(name, roll, perc)

name, roll, perc = ['sravan', 7058, 98.45]
print(name, roll, perc)

# tuples can contain list
tuple1 = ("a", "2", [1, 2, 3])
print(tuple1[2])