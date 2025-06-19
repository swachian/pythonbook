while True:
    age = input("Please tell me the age of the audience? ")
    if age == 'quit':
        break
    else:
        age = int(age)
        if age < 3:
            print(f"The ticket is free for {age} year old audience. ")
        elif age >= 3 and age <= 12:
            print(f"The ticket is 10$ for {age} year old audience. ")
        else:
            print(f"The ticket is 15$ for {age} year old audience. ")

            