code_user = input('please enter a string:\n')

# == 9 ?
code_len = len(code_user)

# first HALF
first_letters = code_user[:code_len // 2]

# last HALF
second_letters = code_user[code_len // 2:]


print(first_letters.lower() + second_letters.upper())
