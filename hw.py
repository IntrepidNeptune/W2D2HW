# Create a list of numbers that are less than ten using l_1 and list comprehension
# Use the following list - [1,11,14,5,8,9]
l_1 = [1,11,14,5,8,9]
l_2 = []

for i in l_1:
    if i < 10:
        l_2.append(i)

print(l_2)

# Using list comprehension, create a list of names of 4 letters or more and capitalize each name
names1 = ['connor', 'connor', 'bob', 'connor', 'evan', 'max', 'evan', 'bob', 'kevin']
names = []

for i in names1:
    if len(i) > 3:
        names.append(i.title())

print(names)
