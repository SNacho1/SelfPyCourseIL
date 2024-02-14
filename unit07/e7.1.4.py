def squared_numbers(start, stop):
    result = []
    num = start
    while num <= stop:
        result.append(num ** 2)
        num += 1
    return result
print(squared_numbers(4, 8))
print(squared_numbers(-3, 3))