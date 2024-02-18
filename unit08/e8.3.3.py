def count_chars(my_str: str) -> dict:
    result = {}

    for single_letter in my_str:
        # להתעלם מרווחים
        if single_letter != " ":
            # אם האות כבר קיימת במילון, נוסיף אחד
            if single_letter in result:
                result[single_letter] += 1
            # אם האות לא קיימת, נתחיל עם אחד
            else:
                result[single_letter] = 1
    return result
            
magic_str = "abra cadabra"
print(count_chars(magic_str))
print(count_chars(magic_str) == {'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1})

