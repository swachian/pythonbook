def commonChars(words):
    result = []
    cache = {}
    length = len(words)
    for word in words:
        cache[word] = list(word)
    for cha in words[0]:
        result.append(cha)
        for word in words:
            if (cha in cache[word]):
                cache[word].remove(cha)
            else:
                result.pop()
                break

    return result           

words = ["bella","label","roller"]
print(commonChars(words))

words = ["cool","lock","cook"]
print(commonChars(words))

# Example 1:

# Input: words = ["bella","label","roller"]
# Output: ["e","l","l"]
# Example 2:

# Input: words = ["cool","lock","cook"]
# Output: ["c","o"]