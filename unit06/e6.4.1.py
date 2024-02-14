def check_valid_input(letter_guessed, old_letters_guessed):
    if len(letter_guessed) != 1 or not letter_guessed.isalpha():
        return False
    if letter_guessed.lower() in old_letters_guessed:
        return False
    return True

old_letters = ['a', 'b', 'c']
print(check_valid_input('C', old_letters)) #False
print(check_valid_input('ep', old_letters)) #False
print(check_valid_input('$', old_letters)) #False
print(check_valid_input('s', old_letters)) #True