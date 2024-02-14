def check_win(secret_word, old_letters_guessed):
    secret_letters_set = set(secret_word)
    guessed_letters_set = set(old_letters_guessed)
    return secret_letters_set.issubset(guessed_letters_set)


secret_word = "friends"
old_letters_guessed = ['m', 'p', 'j', 'i', 's', 'k']
print(check_win(secret_word, old_letters_guessed))
  
secret_word = "yes"
old_letters_guessed = ['d', 'g', 'e', 'i', 's', 'k', 'y']
print(check_win(secret_word, old_letters_guessed))

