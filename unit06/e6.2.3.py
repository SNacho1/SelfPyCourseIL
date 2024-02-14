def format_list(my_list):
    even_elements = my_list[::2]
    last_element = my_list[-1]
    formatted_string = ', '.join(even_elements) + f', and {last_element}'
    return formatted_string

my_list = ["hydrogen", "helium", "lithium", "beryllium", "boron", "magnesium"]
print(format_list(my_list))