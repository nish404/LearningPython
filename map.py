# map() = applies a function to each item in an iterable (list, tuple, etc.)
# map(function, iterable)

store = [("shirt", 20.00),
        ("pants", 45.00),
        ("socks", 18.00),
        ("hoodie", 50.00)]

toEuros = lambda data: (data[0],data[1]*0.82)
toDollars = lambda data:(data[0],data[1]/0.82)

store_euros = list(map(toEuros,store))
store_dollars = list(map(toDollars,store))

for i in store_dollars:
    print(i)
