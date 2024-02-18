def mult_tuple(tuple1, tuple2):
    pairs = [(a, b) for a in tuple1 for b in tuple2] + [(b, a) for a in tuple1 for b in tuple2]
    return tuple(pairs)
first_tuple = (1, 2)
second_tuple = (4, 5)
print(mult_tuple(first_tuple, second_tuple))


first_tuple = (1, 2, 3)
second_tuple = (4, 5, 6)
print(mult_tuple(first_tuple, second_tuple))
