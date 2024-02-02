user_code = input("Enter a palindrome word:\n")
user_code.replace(" ", "")
word_code = user_code[::-1]
if word_code == user_code:
    print("ok")
else:
    print("NOT")