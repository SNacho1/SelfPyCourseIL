def is_valid_input(letter_guessed):
 if letter_guessed > int[0:1] or \
    letter_guessed == '*' '&':
    return False
 
 else:
    letter_guessed == int[0] or \
    letter_guessed != '*' '&'
 return True

print(is_valid_input('a'))
print(is_valid_input('A'))
print(is_valid_input('$'))
print(is_valid_input("ab"))
print(is_valid_input("app$"))





