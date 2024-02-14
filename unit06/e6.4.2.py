def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    if letter_guessed.isalpha() and letter_guessed.lower() not in old_letters_guessed:
        old_letters_guessed.append(letter_guessed.lower())
        return True
    else:
        print("X")
        print(" -> ".join(sorted(old_letters_guessed)))
        return False


old_letters = ['a', 'p', 'c', 'f']
print(try_update_letter_guessed('A', old_letters))
print(try_update_letter_guessed('s', old_letters))
print(old_letters)
print(try_update_letter_guessed('$', old_letters))
print(try_update_letter_guessed('d', old_letters))
print(old_letters)

def display_secret_word(secret_word, letters_guessed):
    displayed_word = ""
    for char in secret_word:
        if char.lower() in letters_guessed:
            displayed_word += char + " "
        else:
            displayed_word += "_ "
    return displayed_word.strip()
secret_word = "banana"
letters_guessed = ['b', 'a', 'n', 'p']
print(display_secret_word(secret_word, letters_guessed))