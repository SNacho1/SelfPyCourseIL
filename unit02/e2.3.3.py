pigs = input("enter 3 digits")
total = int(pigs[0]) + int(pigs[1]) + int(pigs[2])
#another solution
all_pigs = int(pigs)
total2 = all_pigs // 100 +  all_pigs // 10 % 10  + all_pigs % 10

#1
print(total)
#2
print(total // 3)
#3
print(total % 3)
#4
print(total % 3 == 0)
