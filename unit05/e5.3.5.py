def distance(num1: int, num2: int, num3: int):

    first_check = abs(abs(num1) - abs(num2)) == 1 or \
                  abs(abs(num1) - abs(num3)) == 1
 
    second_check = abs(abs(num1) - abs(num2)) >= 2 or \
                   abs(abs(num1) - abs(num3)) >= 2
    
    return first_check and second_check

print(distance(1, 2, 10))
print(distance(4, 5, 3))
