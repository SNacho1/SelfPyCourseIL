def filter_teens(a = 13, b = 13, c = 13):
    return fix_age(a) + fix_age(b) + fix_age(c)

def fix_age(age):
    if age == 13 or age == 14:
        return 0
    elif age == 17 or age == 18 or age == 19:
        return 0
    else:
        return age
 

print(filter_teens()) #0
print(filter_teens(1, 2, 3)) #6
print(filter_teens(2, 13, 1)) #3
print(filter_teens(2, 1, 15)) #18
