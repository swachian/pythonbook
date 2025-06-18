places = ['Great wall', 'Big Ben', 'Greenwich', 'London', 'Paris']

print(places)

sorted_places = sorted(places)

print(f"sorted places {sorted_places}")
print(f"original places {places}")

reverse_sorted_places = sorted(places, reverse = True)

print(f"reverse sorted places {reverse_sorted_places}")

places.reverse()
print(f"change list order {places}")
places.reverse()
print(f"change list order back {places}")
places.sort()
print(f"sort the list self {places}")
places.sort(reverse = True)
print(f"reverse sort the list self {places}")