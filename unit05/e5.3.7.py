def chocolate_maker(small, big, x):
    #      10- 2*5   - 3    
    return x - big*5 - small <= 0


print(chocolate_maker(3, 1, 8)) #True
print(chocolate_maker(3, 1, 9)) #False
print(chocolate_maker(3, 2, 10)) #False