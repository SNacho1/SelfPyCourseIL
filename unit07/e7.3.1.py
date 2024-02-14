def show_hidden_word(secret_word, letters_guessed):
    displayed_word = ""
    for char in secret_word:
        if char.lower() in letters_guessed:
            displayed_word += char + " "
        else:
            displayed_word += "_ "
    return displayed_word.strip()
secret_word = "banana"
letters_guessed = ['b', 'a', 'n', 'p']
print(show_hidden_word(secret_word, letters_guessed))

secret_word = "mammals"
old_letters_guessed = ['s', 'p', 'j', 'i', 'm', 'k']
print(show_hidden_word(secret_word, old_letters_guessed))
