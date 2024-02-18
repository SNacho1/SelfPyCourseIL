def inverse_dict(my_dict: dict) -> dict:
    result = {}
    for tup in my_dict.items():
        if tup[1] in result.keys():
            result[tup[1]].append(tup[0])
        else:
            result[tup[1]] = [tup[0]]
    return result

        


course_dict = {'I': 3, 'love': 3, 'self.py!': 2}
print(inverse_dict(course_dict))
print(inverse_dict(course_dict) == {3: ['I', 'love'], 2: ['self.py!']})