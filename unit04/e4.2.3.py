temp = input('Insert the temperature you would like to convert:\n')
user_type = temp[-1]
user_valio = temp[:-1]

# אם זה פרנהייט
if user_type == 'C' or user_type == 'c':
    result = (9 * int(user_valio) + (32 * 5)) / 5
    print(f"{result}f")
    # אם זה צלזיוס
elif user_type == 'F' or user_type == 'f':
    result = (5 * int(user_valio) - 160) / 9
    print(f"{result}c")
else:
    print("You did not write the temperature correctly, try again")