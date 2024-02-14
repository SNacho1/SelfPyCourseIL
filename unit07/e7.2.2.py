def numbers_letters_count(my_str):
    digits_count = sum(c.isdigit() for c in my_str)
    letters_count = sum(c.isalpha() for c in my_str)
    return [digits_count, letters_count]
print(numbers_letters_count("Python 3.6.3"))