available_corps = ['Apple', 'YY', 'TT', 'Nvidia']
requested_corps = ['Nvidia', 'Apple', 'Ctrip']

for requested_corp in requested_corps:
    if (requested_corp in available_corps):
        print(f"{requested_corp} will give you an offer")
    else:
        print(f"Sorry, {requested_corp} has closed.")

corps = []
if not corps:
    print("We need to find some users!")

numbers = list(range(1, 10))
for number in numbers:
    if number == 1:
        print("1st")
    elif number == 2:
        print("2nd")        
    elif number == 3:
        print("3rd")
    elif number >= 4 and number <=9:
        print(f"{number}th")  


