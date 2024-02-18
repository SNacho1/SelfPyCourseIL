mariah_dict = {
    'first_name': 'Mariah',
    'last_name': 'Carey',
    'birth_date': '27.03.1970',
    'hobbies': ['sing', 'Compose', 'act']
}
#1
last_name = mariah_dict["last_name"]
print(last_name)
#2
birth_month = int(mariah_dict["birth_date"].split('.')[1])
print(birth_month)
#3
num_hobbies = len(mariah_dict["hobbies"])
print(num_hobbies)
#4
last_hobbie = mariah_dict["hobbies"][-1]
print(last_hobbie)
#5
mariah_dict["hobbies"].append("Cooking")
#6
birth_date_parts = mariah_dict["birth_date"].split('.')
birth_date_tuple = tuple(int(part) for part in birth_date_parts[::-1])
print(birth_date_tuple)
#7
from datetime import datetime
birthdate = datetime.strptime(mariah_dict["birth_date"], "%d.%m.%Y")
today = datetime.now()
age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
mariah_dict["age"] = age
print(age)

choice = int(input("please enter a num between 1-7"))
if choice == 1:
    print (last_name)
if choice == 2:
    print(birth_month)
if choice == 3:
    print(num_hobbies)
if choice == 4:
    print(last_hobbie)
if choice == 5:
    print(mariah_dict["hobbies"])
if choice == 6:
    print(birth_date_tuple)
if choice == 7:
    print(age)
else:
    print("you have to chose a num between 1-7")
