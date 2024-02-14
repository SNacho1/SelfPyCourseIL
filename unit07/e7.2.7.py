def arrow(my_char, max_length):
    arrow_string = ''
    for i in range(1, max_length + 1):
        arrow_string += (my_char + '') * i + '\n'
    for i in range(max_length - 1, 0, -1):
        arrow_string += (my_char + '') * i + '\n'
    return arrow_string

print(arrow('*', 5))
