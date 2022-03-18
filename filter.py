# filter() = creates a collection of elements from an iterable for which a function returns true
# filter(function,iterable)

friends = [("friend1", 28),
            ("friend2", 30),
            ("friend3", 24),
            ("friend4", 34),
            ("friend5", 40)]

age = lambda data:data[1] >= 25

list(filter(age, friends))

buddies = list(filter(age, friends))

for i in buddies:
    print(i)
