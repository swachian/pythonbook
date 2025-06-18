# Practise list functions
people_names = ['Lifeifei', 'Yuanli', 'Xuchengang', '张学友']

for name in people_names:
    print(f"Do you have time to attend my dinner, {name}")

failed_person = 'Yuanli'
new_person = '刘德华'
print(f"{failed_person} can't come, {new_person} will be invited")

index = people_names.index(failed_person)
people_names.insert(index, new_person)
people_names.remove(failed_person)

print("I have got more tables so that I can invite more people")
people_names.append('David')
people_names.insert(3, 'Uncle Bob')
people_names.insert(0, 'Vlad')
for name in people_names:
    print(f"Do you have time to attend my dinner, {name}")

print(f"Now I invite {len(people_names)} people.")
print("The table is not being sent in time, so I have reduce the number of people to my dinner")

sorry_name = people_names.pop()
print(f"I genuisely feel sorry that I can't invite you now, {sorry_name}")

sorry_name = people_names.pop()
print(f"I genuisely feel sorry that I can't invite you now, {sorry_name}")
sorry_name = people_names.pop()
print(f"I genuisely feel sorry that I can't invite you now, {sorry_name}")
sorry_name = people_names.pop()
print(f"I genuisely feel sorry that I can't invite you now, {sorry_name}")
sorry_name = people_names.pop()
print(f"I genuisely feel sorry that I can't invite you now, {sorry_name}")

for name in people_names:
    print(f"Do you have time to attend my dinner, {name}")

del people_names[0]
del people_names[0]