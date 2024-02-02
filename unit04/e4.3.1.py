guess = input("guess the letter:\n")

if len(guess) > 1 and ('&' in guess or '*' in guess ):
    print('E3 - man, you have a LOT of chars AND weird letters')
elif len(guess) > 1:
    print(f'E1 - you entered {len(guess)} instead of 1')
elif '&' in guess or '*' in guess:
    print('E2 - man, you have some weird letters!')
else:
    print(guess.lower())