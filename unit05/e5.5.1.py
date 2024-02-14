def is_valid_input(letter_guessed):

   if len(letter_guessed) > 1 and ('&' in letter_guessed or '*' in letter_guessed or '$' in letter_guessed):
    return False

   elif len(letter_guessed) > 1:
    return False
 
   elif '&' in letter_guessed or '*' in letter_guessed or '$' in letter_guessed:
    return False
 
   else:
    return True
print(is_valid_input('a'))
print(is_valid_input('A'))
print(is_valid_input('$'))
print(is_valid_input("ab"))
print(is_valid_input("app$"))