# 2025.06.16 Practise list with numbers
for i in range(21):
    print(i)

# for i in range(1000000):
#     print(i)

numbers = list(range(1000001))
print(f"The sum of {min(numbers)} to {max(numbers)} is {sum(numbers)}")

for i in range(1, 20, 2):
    print(i)

three_muliples = [value * 3 for value in range(1, 11)]
for number in three_muliples:
    print(number)

cube_numbers = [value ** 3 for value in range(1, 11)]
for number in cube_numbers:
    print(number)