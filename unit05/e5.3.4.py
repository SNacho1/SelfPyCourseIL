def last_early(my_str): 
    my_str = my_str.lower()
    last_char =  my_str[-1]

    if last_char in my_str[0:-1]:
        return True
    else:
        return False

print(last_early("happy birthday"))
print(last_early("best of luck"))
print(last_early("Wow"))
print(last_early("X"))