code_user = input('Please enter a string:\n')
first_char = code_user[0]
result = first_char + code_user[1:].replace(first_char,'e')
print(result)
