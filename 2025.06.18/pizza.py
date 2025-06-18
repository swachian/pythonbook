# 2025.06.18 Practise list iterator
pizzas = ['Magret', 'Tomato', 'Beckon']

for pizza in pizzas:
    print(f"I like {pizza} pizza")

print("I really love c#")

animals = ['dog', 'cat', 'horse']
for animal in animals:
    print(f"{animal} is lovable!")
print("Any of these animals have 4 legs.")



    def commonChars(self, words):
        result = {}
        length = len(words)
        for i in range(0, length):
            for characater in words[i]:
                result[characater] = True
                for j in range(i, length):
                    if character not in words[j]:
                        del result[characater]
        return result.keys()           
               
        